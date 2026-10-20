export const Navbar = () => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 sticky top-0 z-50 shadow-md">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white shadow-indigo-500/30 shadow-lg">
            P
          </div>
          <span className="text-xl font-bold text-white tracking-tight">
            Catálogo<span className="text-indigo-400">Pro</span>
          </span>
        </div>
        <span className="text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
          Unidad 5 • TUPaD
        </span>
      </div>
    </header>
  );
};
