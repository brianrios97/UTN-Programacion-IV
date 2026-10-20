export const Footer = () => {
  return (
    <footer className="bg-slate-900 border-t border-slate-800 py-6 mt-16 text-center text-sm text-slate-400">
      <div className="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-4">
        <p className="text-xs text-slate-500">
          © 2026 CatálogoPro — Tecnicatura Universitaria en Programación a Distancia (UTN).
        </p>
        <div className="flex items-center gap-4 text-xs font-medium text-slate-400">
          <span>React 19</span>
          <span>•</span>
          <span>TypeScript</span>
          <span>•</span>
          <span>Tailwind CSS v4</span>
        </div>
      </div>
    </footer>
  );
};
