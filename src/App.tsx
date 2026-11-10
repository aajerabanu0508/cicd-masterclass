import React, { useState, useEffect } from 'react';
import { useProgress } from './hooks/useProgress';
import { Navbar } from './components/Navbar';
import { HomePage } from './pages/HomePage';
import { LessonPage } from './pages/LessonPage';
import { SimulatorPage } from './pages/SimulatorPage';
import { ReferencePage } from './pages/ReferencePage';
import { PresentationPage } from './pages/PresentationPage';
import { AwsSimulatorPage } from './pages/AwsSimulatorPage';
import { SearchModal } from './components/SearchModal';
import { CertificateModal } from './components/CertificateModal';
import { lessons } from './content/lessons';
import { Rocket } from 'lucide-react';

export function App() {
  const {
    progress,
    toggleComplete,
    markComplete,
    recordQuizAnswer,
    toggleBookmark,
    setUserName,
    percentComplete,
  } = useProgress();

  const [currentView, setCurrentView] = useState<'home' | 'lesson' | 'simulator' | 'aws' | 'reference' | 'presentation'>('home');
  const [currentLessonSlug, setCurrentLessonSlug] = useState<string>(lessons[0].slug);
  const [searchModalOpen, setSearchModalOpen] = useState(false);
  const [certModalOpen, setCertModalOpen] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // Parse URL hash for bookmarkable routing
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash.replace('#', '');
      if (!hash || hash === 'home') {
        setCurrentView('home');
      } else if (hash === 'simulator') {
        setCurrentView('simulator');
      } else if (hash === 'aws' || hash === 'aws-simulator') {
        setCurrentView('aws');
      } else if (hash === 'reference') {
        setCurrentView('reference');
      } else if (hash === 'presentation') {
        setCurrentView('presentation');
      } else if (hash.startsWith('lesson/')) {
        const slug = hash.replace('lesson/', '');
        const exists = lessons.some((l) => l.slug === slug);
        if (exists) {
          setCurrentLessonSlug(slug);
          setCurrentView('lesson');
        }
      }
    };

    handleHashChange();
    window.addEventListener('hashchange', handleHashChange);
    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  const navigateTo = (view: 'home' | 'lesson' | 'simulator' | 'aws' | 'reference' | 'presentation', lessonSlug?: string) => {
    setCurrentView(view);
    setMobileMenuOpen(false);

    if (view === 'home') {
      window.location.hash = 'home';
    } else if (view === 'simulator') {
      window.location.hash = 'simulator';
    } else if (view === 'aws') {
      window.location.hash = 'aws';
    } else if (view === 'reference') {
      window.location.hash = 'reference';
    } else if (view === 'presentation') {
      window.location.hash = 'presentation';
    } else if (view === 'lesson') {
      const targetSlug = lessonSlug || currentLessonSlug;
      setCurrentLessonSlug(targetSlug);
      window.location.hash = `lesson/${targetSlug}`;
    }
  };

  const handleSelectLessonFromSearch = (slug: string) => {
    navigateTo('lesson', slug);
  };

  return (
    <div className="min-h-screen bg-[#f8fafc] text-slate-900 flex flex-col font-sans selection:bg-blue-500/20 selection:text-blue-900">
      {/* Top Navbar */}
      <Navbar
        currentView={currentView}
        onNavigate={navigateTo}
        percentComplete={percentComplete}
        onOpenSearch={() => setSearchModalOpen(true)}
        onOpenCertificate={() => setCertModalOpen(true)}
        mobileMenuOpen={mobileMenuOpen}
        onToggleMobileMenu={() => setMobileMenuOpen(!mobileMenuOpen)}
      />

      {/* Mobile Navigation Drawer */}
      {mobileMenuOpen && (
        <div className="md:hidden bg-white border-b border-slate-200 px-4 py-4 space-y-2 animate-fadeIn z-30 shadow-md">
          <button
            onClick={() => navigateTo('home')}
            className="w-full text-left px-3 py-2 text-sm rounded-lg text-slate-700 hover:bg-slate-100 font-medium"
          >
            🏠 Course Overview
          </button>
          <button
            onClick={() => navigateTo('lesson', currentLessonSlug)}
            className="w-full text-left px-3 py-2 text-sm rounded-lg text-slate-700 hover:bg-slate-100 font-medium"
          >
            📖 Continue Lessons
          </button>
          <button
            onClick={() => navigateTo('simulator')}
            className="w-full text-left px-3 py-2 text-sm rounded-lg text-blue-600 font-semibold hover:bg-slate-100"
          >
            ⚡ Pipeline Simulator
          </button>
          <button
            onClick={() => navigateTo('aws')}
            className="w-full text-left px-3 py-2 text-sm rounded-lg text-amber-700 font-bold hover:bg-amber-50"
          >
            ☁️ AWS Cloud Lab (ECS & OIDC)
          </button>
          <button
            onClick={() => navigateTo('reference')}
            className="w-full text-left px-3 py-2 text-sm rounded-lg text-slate-700 hover:bg-slate-100 font-medium"
          >
            📋 Cheatsheets & Glossary
          </button>
          <button
            onClick={() => navigateTo('presentation')}
            className="w-full text-left px-3 py-2 text-sm rounded-lg text-amber-800 font-bold hover:bg-amber-50"
          >
            📽️ PPT Slides (21)
          </button>
        </div>
      )}

      {/* Main Body */}
      <div className={`flex-1 ${currentView === 'presentation' ? 'flex flex-col justify-center' : ''}`}>
        {currentView === 'home' && (
          <HomePage
            onStartCourse={(slug) => navigateTo('lesson', slug || currentLessonSlug)}
            onOpenSimulator={() => navigateTo('simulator')}
            onOpenAws={() => navigateTo('aws')}
            onOpenReference={() => navigateTo('reference')}
            completedLessons={progress.completedLessons}
            percentComplete={percentComplete}
          />
        )}

        {currentView === 'lesson' && (
          <LessonPage
            currentLessonSlug={currentLessonSlug}
            onSelectLesson={(slug) => navigateTo('lesson', slug)}
            completedLessons={progress.completedLessons}
            bookmarks={progress.bookmarks}
            quizScores={progress.quizScores}
            onToggleComplete={toggleComplete}
            onToggleBookmark={toggleBookmark}
            onAnswerQuiz={recordQuizAnswer}
            onBackToOverview={() => navigateTo('home')}
          />
        )}

        {currentView === 'simulator' && (
          <SimulatorPage onBackToCourse={() => navigateTo('lesson', currentLessonSlug)} />
        )}

        {currentView === 'aws' && (
          <AwsSimulatorPage 
            onBackToCourse={() => navigateTo('home')} 
            onOpenPresentation={() => navigateTo('presentation')}
          />
        )}

        {currentView === 'reference' && <ReferencePage />}
        {currentView === 'presentation' && <PresentationPage onBackToCourse={() => navigateTo('home')} />}
      </div>

      {/* Global Modals */}
      <SearchModal
        isOpen={searchModalOpen}
        onClose={() => setSearchModalOpen(false)}
        onSelectLesson={handleSelectLessonFromSearch}
      />

      <CertificateModal
        isOpen={certModalOpen}
        onClose={() => setCertModalOpen(false)}
        userName={progress.userName}
        onUpdateName={setUserName}
        percentComplete={percentComplete}
      />

      {/* Modern Global Footer (Hidden in Presentation Deck View for Clean UX) */}
      {currentView !== 'presentation' && (
        <footer className="bg-slate-100 border-t border-slate-200 py-10 px-4 mt-auto">
          <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6 text-xs text-slate-600">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-blue-600 via-indigo-600 to-cyan-500 flex items-center justify-center text-white shadow-sm shrink-0">
              <Rocket className="w-4 h-4 text-white -rotate-12" />
            </div>
            <div>
              <span className="font-bold text-slate-900 text-sm">CI/CD Masterclass</span>
              <p className="text-[11px] text-slate-500">Automated Cloud Deployment & DevOps Delivery</p>
            </div>
          </div>

          <div className="flex items-center gap-6">
            <button onClick={() => navigateTo('home')} className="hover:text-blue-600 font-medium transition-colors">
              Overview
            </button>
            <button onClick={() => navigateTo('lesson', 'introduction-to-cicd')} className="hover:text-blue-600 font-medium transition-colors">
              Lessons (20)
            </button>
            <button onClick={() => navigateTo('simulator')} className="hover:text-blue-600 font-medium transition-colors">
              Simulator
            </button>
            <button onClick={() => navigateTo('aws')} className="hover:text-amber-700 font-bold transition-colors">
              AWS Cloud Lab
            </button>
            <button onClick={() => navigateTo('reference')} className="hover:text-blue-600 font-medium transition-colors">
              Glossary
            </button>
            <button onClick={() => navigateTo('presentation')} className="hover:text-amber-700 font-bold transition-colors">
              PPT Slides (21)
            </button>
            <button onClick={() => setCertModalOpen(true)} className="hover:text-amber-700 font-medium transition-colors">
              Certificate
            </button>
          </div>

          <div className="text-center md:text-right text-slate-500">
            <span>Built with React 18, TypeScript, and Tailwind CSS</span>
          </div>
        </div>
      </footer>
      )}
    </div>
  );
}

export default App;
