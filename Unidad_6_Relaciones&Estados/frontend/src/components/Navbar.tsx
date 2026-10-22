export const Navbar = () => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 sticky top-0 z-40 shadow-sm">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-lg bg-indigo-600 flex items-center justify-center font-bold text-white shadow-indigo-500/20 shadow-md">
            C
          </div>
          <div>
            <span className="text-lg font-bold text-white tracking-tight">
              Catálogo<span className="text-indigo-400">Pro</span>
            </span>
            <span className="hidden sm:inline-block text-xs text-slate-400 ml-2 font-medium">
              | Gestor de Categorías
            </span>
          </div>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs font-semibold px-3 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
            Unidad 6 • Relaciones y Estado
          </span>
        </div>
      </div>
    </header>
  );
};
