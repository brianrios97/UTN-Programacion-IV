import React from 'react';
import { Link } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export const UnauthorizedPage: React.FC = () => {
  const { user } = useAuthStore();

  return (
    <div className="flex min-h-[calc(100vh-4rem)] items-center justify-center bg-slate-50 px-4 py-12">
      <div className="w-full max-w-md text-center rounded-2xl bg-white p-8 shadow-xl border border-slate-100">
        <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-amber-100 text-amber-600">
          <svg
            className="h-8 w-8"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth="1.5"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M12 9v3.75m0-10.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.75c0 5.592 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.57-.598-3.75h-.152c-3.196 0-6.1-1.249-8.25-3.286zm0 13.036h.008v.008H12v-.008z"
            />
          </svg>
        </div>

        <h1 className="mt-4 text-3xl font-extrabold tracking-tight text-slate-900">
          Acceso denegado
        </h1>
        <p className="mt-2 text-sm text-slate-500">
          No tienes los permisos necesarios para acceder a este recurso. Esta sección está reservada exclusivamente para usuarios con rol administrador.
        </p>

        {user && (
          <div className="mt-4 inline-block rounded-md bg-slate-100 px-3 py-1.5 text-xs font-medium text-slate-700">
            Tu rol actual: <span className="font-bold uppercase text-indigo-700">{user.role}</span>
          </div>
        )}

        <div className="mt-6 flex justify-center gap-3">
          <Link
            to="/categories"
            className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white shadow hover:bg-indigo-500 transition"
          >
            Ir a Categorías
          </Link>
          <Link
            to="/"
            className="rounded-lg border border-slate-300 bg-white px-4 py-2 text-sm font-semibold text-slate-700 hover:bg-slate-50 transition"
          >
            Inicio
          </Link>
        </div>
      </div>
    </div>
  );
};

export default UnauthorizedPage;
