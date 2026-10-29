import React from 'react';
import { Link, NavLink, useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export const Navbar: React.FC = () => {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate('/login');
  };

  const navLinkClass = ({ isActive }: { isActive: boolean }) =>
    `px-3 py-2 rounded-md text-sm font-medium transition-colors ${
      isActive
        ? 'bg-indigo-700 text-white shadow-sm'
        : 'text-indigo-100 hover:bg-indigo-600 hover:text-white'
    }`;

  return (
    <header className="sticky top-0 z-50 bg-indigo-900 shadow-md">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
        <div className="flex items-center gap-6">
          <Link to="/" className="flex items-center gap-2 text-xl font-bold tracking-tight text-white">
            <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-500 font-black text-white shadow">
              FS
            </span>
            <span>Food Store</span>
          </Link>

          {user && (
            <nav className="hidden md:flex items-center space-x-2">
              <NavLink to="/categories" className={navLinkClass}>
                Categorías
              </NavLink>
              <NavLink to="/products" className={navLinkClass}>
                Productos
              </NavLink>
              <NavLink to="/ingredients" className={navLinkClass}>
                Ingredientes
              </NavLink>
              {user.role === 'admin' && (
                <NavLink to="/admin/users" className={navLinkClass}>
                  Usuarios (Admin)
                </NavLink>
              )}
            </nav>
          )}
        </div>

        <div className="flex items-center gap-4">
          {user ? (
            <div className="flex items-center gap-3">
              <div className="flex flex-col text-right">
                <span className="text-sm font-semibold text-white">
                  {user.full_name || user.username}
                </span>
                <div className="flex items-center justify-end gap-1">
                  <span
                    className={`inline-flex items-center px-2 py-0.5 rounded text-xs font-bold uppercase tracking-wider ${
                      user.role === 'admin'
                        ? 'bg-amber-400 text-amber-950'
                        : 'bg-indigo-200 text-indigo-950'
                    }`}
                  >
                    {user.role}
                  </span>
                </div>
              </div>

              <button
                onClick={handleLogout}
                className="inline-flex items-center justify-center rounded-md bg-rose-600 px-3 py-1.5 text-xs font-semibold text-white shadow-sm hover:bg-rose-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-rose-600 transition"
              >
                Cerrar sesión
              </button>
            </div>
          ) : (
            <div className="flex items-center space-x-3">
              <Link
                to="/login"
                className="text-sm font-medium text-indigo-200 hover:text-white"
              >
                Iniciar sesión
              </Link>
              <Link
                to="/register"
                className="rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500"
              >
                Registrarse
              </Link>
            </div>
          )}
        </div>
      </div>

      {/* Mobile nav */}
      {user && (
        <div className="flex md:hidden border-t border-indigo-800 px-4 py-2 space-x-2 overflow-x-auto">
          <NavLink to="/categories" className={navLinkClass}>
            Categorías
          </NavLink>
          <NavLink to="/products" className={navLinkClass}>
            Productos
          </NavLink>
          <NavLink to="/ingredients" className={navLinkClass}>
            Ingredientes
          </NavLink>
          {user.role === 'admin' && (
            <NavLink to="/admin/users" className={navLinkClass}>
              Usuarios
            </NavLink>
          )}
        </div>
      )}
    </header>
  );
};

export default Navbar;
