import React from 'react';
import { 
  Sparkles, 
  Search, 
  Award, 
  Terminal, 
  BookOpen, 
  Menu, 
  X, 
  Home, 
  Layers, 
  Cloud,
  ChevronRight,
  Tv
} from 'lucide-react';

interface NavbarProps {
  currentView: 'home' | 'lesson' | 'simulator' | 'aws' | 'reference' | 'presentation';
  onNavigate: (view: 'home' | 'lesson' | 'simulator' | 'aws' | 'reference' | 'presentation', lessonSlug?: string) => void;
  percentComplete: number;
  onOpenSearch: () => void;
  onOpenCertificate: () => void;
  mobileMenuOpen: boolean;
  onToggleMobileMenu: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentView,
  onNavigate,
  percentComplete,
  onOpenSearch,
  onOpenCertificate,
  mobileMenuOpen,
  onToggleMobileMenu,
}) => {
  return (
    <header className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/90 shadow-2xs">
      <div className="w-full max-w-7xl 2xl:max-w-[1600px] mx-auto px-3 sm:px-5 lg:px-8 h-16 flex items-center justify-between gap-2 sm:gap-4">
        
        {/* =========================================================================
            LEFT: BRAND LOGO & TITLE
            ========================================================================= */}
        <div className="flex items-center gap-2 sm:gap-3 shrink-0">
          <button
            onClick={() => onNavigate('home')}
            className="flex items-center gap-2.5 sm:gap-3 text-left group focus:outline-none"
            title="CI/CD Masterclass Home"
          >
            <div className="relative shrink-0">
              <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-tr from-amber-400 to-orange-500 flex items-center justify-center text-slate-950 font-black shadow-md shadow-orange-500/20 group-hover:scale-105 transition-transform">
                <span className="text-lg sm:text-xl">🍔</span>
              </div>
              <span className="absolute -bottom-0.5 -right-0.5 flex h-2.5 w-2.5">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-blue-600"></span>
              </span>
            </div>

            <div className="flex flex-col justify-center">
              <div className="flex items-center gap-1.5">
                <span className="font-black text-sm sm:text-base md:text-lg text-slate-950 tracking-tight whitespace-nowrap">
                  CI/CD <span className="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">Masterclass</span>
                </span>
                <span className="text-[10px] font-mono uppercase bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded-full font-bold hidden xs:inline-block">
                  20 Lessons
                </span>
              </div>
              <p className="text-[10px] text-slate-500 hidden xl:block font-medium truncate max-w-[240px]">
                Food Delivery to Cloud Pipelines
              </p>
            </div>
          </button>
        </div>

        {/* =========================================================================
            CENTER: DESKTOP NAVIGATION SEGMENTED PILLS (RESPONSIVE)
            ========================================================================= */}
        <nav className="hidden lg:flex items-center gap-1 bg-slate-100/90 p-1 rounded-xl border border-slate-200/80 shadow-inner">
          {/* 1. Overview */}
          <button
            onClick={() => onNavigate('home')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 whitespace-nowrap ${
              currentView === 'home'
                ? 'bg-white text-blue-700 border border-slate-200 shadow-xs'
                : 'text-slate-600 hover:text-slate-950 hover:bg-white/70'
            }`}
          >
            <Home className="w-3.5 h-3.5 text-blue-600 shrink-0" />
            <span>Overview</span>
          </button>

          {/* 2. Lessons */}
          <button
            onClick={() => onNavigate('lesson', 'introduction-to-cicd')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 whitespace-nowrap ${
              currentView === 'lesson'
                ? 'bg-white text-blue-700 border border-slate-200 shadow-xs'
                : 'text-slate-600 hover:text-slate-950 hover:bg-white/70'
            }`}
          >
            <BookOpen className="w-3.5 h-3.5 text-indigo-600 shrink-0" />
            <span>Lessons</span>
          </button>

          {/* 3. Pipeline Simulator */}
          <button
            onClick={() => onNavigate('simulator')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 whitespace-nowrap ${
              currentView === 'simulator'
                ? 'bg-white text-blue-700 border border-slate-200 shadow-xs'
                : 'text-slate-600 hover:text-slate-950 hover:bg-white/70'
            }`}
          >
            <Terminal className="w-3.5 h-3.5 text-blue-600 shrink-0" />
            <span>Simulator</span>
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
          </button>

          {/* 4. AWS Cloud Lab */}
          <button
            onClick={() => onNavigate('aws')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 whitespace-nowrap ${
              currentView === 'aws'
                ? 'bg-amber-400 text-slate-950 shadow-xs'
                : 'text-amber-900 hover:text-amber-950 hover:bg-amber-100/60'
            }`}
          >
            <Cloud className="w-3.5 h-3.5 text-amber-600 shrink-0" />
            <span>AWS Lab</span>
            <span className="text-[9px] bg-amber-200/90 text-amber-950 px-1 py-0.2 rounded font-mono font-bold">ECS</span>
          </button>

          {/* 5. Cheat Sheet */}
          <button
            onClick={() => onNavigate('reference')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 whitespace-nowrap ${
              currentView === 'reference'
                ? 'bg-white text-blue-700 border border-slate-200 shadow-xs'
                : 'text-slate-600 hover:text-slate-950 hover:bg-white/70'
            }`}
          >
            <Layers className="w-3.5 h-3.5 text-slate-500 shrink-0" />
            <span>Cheat Sheet</span>
          </button>

          {/* 6. Slides Deck */}
          <button
            onClick={() => onNavigate('presentation')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 whitespace-nowrap ${
              currentView === 'presentation'
                ? 'bg-blue-600 text-white shadow-xs'
                : 'text-blue-700 hover:text-blue-900 hover:bg-blue-50'
            }`}
            title="Interactive Presentation Slide Decks"
          >
            <Tv className="w-3.5 h-3.5 shrink-0" />
            <span>Slides Deck</span>
          </button>
        </nav>

        {/* =========================================================================
            RIGHT: SEARCH, CERTIFICATE, PROGRESS & MOBILE TRIGGER
            ========================================================================= */}
        <div className="flex items-center gap-1.5 sm:gap-2.5 shrink-0">
          {/* Quick Search Button */}
          <button
            onClick={onOpenSearch}
            className="flex items-center gap-1.5 sm:gap-2 bg-slate-50 hover:bg-slate-100 border border-slate-200 hover:border-slate-300 text-slate-700 px-2.5 sm:px-3 py-1.5 rounded-xl text-xs font-medium transition-all shadow-2xs"
            title="Search lessons (⌘K)"
          >
            <Search className="w-3.5 h-3.5 text-blue-600 shrink-0" />
            <span className="hidden sm:inline font-medium">Search...</span>
            <kbd className="hidden md:inline-block text-[10px] bg-white text-slate-500 px-1.5 py-0.5 rounded border border-slate-200 font-mono shadow-2xs">
              ⌘K
            </kbd>
          </button>

          {/* Certificate Award Button */}
          <button
            onClick={onOpenCertificate}
            className="flex items-center gap-1 sm:gap-1.5 px-2.5 sm:px-3 py-1.5 bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 rounded-xl text-xs font-bold transition-all shadow-2xs"
            title="View Course Completion Certificate"
          >
            <Award className="w-3.5 h-3.5 text-amber-600 shrink-0" />
            <span className="hidden md:inline">Certificate</span>
          </button>

          {/* Circular Progress Badge */}
          <div 
            className="flex items-center gap-1.5 bg-slate-50 border border-slate-200 px-2 sm:px-2.5 py-1 rounded-xl shadow-2xs"
            title={`Course Progress: ${percentComplete}% completed`}
          >
            <div className="w-5 h-5 sm:w-5.5 sm:h-5.5 relative flex items-center justify-center shrink-0">
              <svg className="w-full h-full -rotate-90" viewBox="0 0 36 36">
                <path
                  className="text-slate-200"
                  strokeWidth="4"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  className="text-blue-600 transition-all duration-500"
                  strokeDasharray={`${percentComplete}, 100`}
                  strokeWidth="4"
                  strokeLinecap="round"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
            </div>
            <span className="text-xs font-mono font-bold text-slate-800">{percentComplete}%</span>
          </div>

          {/* Mobile Menu Hamburger (Visible on screens < lg) */}
          <button
            onClick={onToggleMobileMenu}
            className="lg:hidden p-2 rounded-xl text-slate-700 hover:text-slate-950 bg-slate-100 hover:bg-slate-200 border border-slate-200 transition-colors"
            title="Toggle Menu"
          >
            {mobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
          </button>
        </div>
      </div>

      {/* =========================================================================
          MOBILE / TABLET SLIDE-DOWN DRAWER (WHEN MENU IS OPEN)
          ========================================================================= */}
      {mobileMenuOpen && (
        <div className="lg:hidden border-t border-slate-200 bg-white/98 backdrop-blur-lg px-4 py-3 shadow-xl animate-fadeIn space-y-2">
          <div className="grid grid-cols-2 gap-2 pb-2 border-b border-slate-100">
            <button
              onClick={() => onNavigate('home')}
              className={`p-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${
                currentView === 'home'
                  ? 'bg-blue-50 text-blue-800 border-blue-200'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span className="flex items-center gap-2">
                <Home className="w-4 h-4 text-blue-600" />
                <span>Overview</span>
              </span>
              <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
            </button>

            <button
              onClick={() => onNavigate('lesson', 'introduction-to-cicd')}
              className={`p-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${
                currentView === 'lesson'
                  ? 'bg-blue-50 text-blue-800 border-blue-200'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span className="flex items-center gap-2">
                <BookOpen className="w-4 h-4 text-indigo-600" />
                <span>Lessons</span>
              </span>
              <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
            </button>

            <button
              onClick={() => onNavigate('simulator')}
              className={`p-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${
                currentView === 'simulator'
                  ? 'bg-blue-50 text-blue-800 border-blue-200'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span className="flex items-center gap-2">
                <Terminal className="w-4 h-4 text-blue-600" />
                <span>Simulator</span>
              </span>
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            </button>

            <button
              onClick={() => onNavigate('aws')}
              className={`p-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${
                currentView === 'aws'
                  ? 'bg-amber-100 text-amber-950 border-amber-300'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span className="flex items-center gap-2">
                <Cloud className="w-4 h-4 text-amber-600" />
                <span>AWS Lab</span>
              </span>
              <span className="text-[9px] bg-amber-200 text-amber-950 px-1 py-0.2 rounded font-bold">ECS</span>
            </button>

            <button
              onClick={() => onNavigate('reference')}
              className={`p-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${
                currentView === 'reference'
                  ? 'bg-blue-50 text-blue-800 border-blue-200'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span className="flex items-center gap-2">
                <Layers className="w-4 h-4 text-slate-500" />
                <span>Cheat Sheet</span>
              </span>
              <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
            </button>

            <button
              onClick={() => onNavigate('presentation')}
              className={`p-2.5 rounded-xl text-xs font-bold flex items-center justify-between border transition-all ${
                currentView === 'presentation'
                  ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span className="flex items-center gap-2">
                <Tv className="w-4 h-4 text-blue-500" />
                <span>Slides Deck</span>
              </span>
              <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-blue-100 text-blue-800 font-bold">
                21+10
              </span>
            </button>
          </div>

          {/* Mobile Bottom Actions */}
          <div className="flex items-center justify-between gap-2 pt-1">
            <button
              onClick={onOpenSearch}
              className="flex-1 py-2 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-xs font-bold text-slate-700 flex items-center justify-center gap-2"
            >
              <Search className="w-3.5 h-3.5 text-blue-600" />
              <span>Search Curriculum (⌘K)</span>
            </button>
            <button
              onClick={onOpenCertificate}
              className="py-2 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 border border-amber-200 text-xs font-bold text-amber-900 flex items-center justify-center gap-1.5"
            >
              <Award className="w-3.5 h-3.5 text-amber-600" />
              <span>Certificate</span>
            </button>
          </div>
        </div>
      )}
    </header>
  );
};
