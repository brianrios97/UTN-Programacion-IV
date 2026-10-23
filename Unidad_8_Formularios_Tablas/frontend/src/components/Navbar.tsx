import { Link, NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <header className="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <Link to="/categorias" className="flex items-center gap-3 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 to-teal-400 flex items-center justify-center shadow-lg shadow-emerald-500/20 group-hover:scale-105 transition-transform duration-200">
              <svg className="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
              </svg>
            </div>
            <div>
              <span className="text-xl font-bold bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">
                FoodStore
              </span>
              <span className="hidden sm:inline-block ml-2 px-2 py-0.5 text-xs font-medium rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                U8 Formularios &amp; Tablas
              </span>
            </div>
          </Link>

          <nav className="flex items-center gap-1 sm:gap-2">
            <NavLink
              to="/categorias"
              className={({ isActive }) =>
                `px-3 sm:px-4 py-2 rounded-xl text-sm font-medium transition-all duration-150 flex items-center gap-2 ${
                  isActive
                    ? 'bg-emerald-500 text-white shadow-md shadow-emerald-500/25 font-semibold'
                    : 'text-slate-300 hover:text-white hover:bg-slate-800'
                }`
              }
            >
              <span>Categor?as</span>
            </NavLink>

            <NavLink
              to="/productos"
              className={({ isActive }) =>
                `px-3 sm:px-4 py-2 rounded-xl text-sm font-medium transition-all duration-150 flex items-center gap-2 ${
                  isActive
                    ? 'bg-emerald-500 text-white shadow-md shadow-emerald-500/25 font-semibold'
                    : 'text-slate-300 hover:text-white hover:bg-slate-800'
                }`
              }
            >
              <span>Productos</span>
            </NavLink>

            <NavLink
              to="/ingredientes"
              className={({ isActive }) =>
                `px-3 sm:px-4 py-2 rounded-xl text-sm font-medium transition-all duration-150 flex items-center gap-2 ${
                  isActive
                    ? 'bg-emerald-500 text-white shadow-md shadow-emerald-500/25 font-semibold'
                    : 'text-slate-300 hover:text-white hover:bg-slate-800'
                }`
              }
            >
              <span>Ingredientes</span>
            </NavLink>
          </nav>
        </div>
      </div>
    </header>
  );
}
