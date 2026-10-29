import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useForm } from '@tanstack/react-form';
import { useAuthStore } from '../store/authStore';

export const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const { login, isLoading } = useAuthStore();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const form = useForm({
    defaultValues: {
      username: '',
      password: '',
    },
    onSubmit: async ({ value }) => {
      setErrorMessage(null);
      try {
        await login(value);
        navigate('/categories');
      } catch (err: any) {
        const detail =
          err.response?.data?.detail ||
          err.message ||
          'Credenciales inválidas. Por favor verifique sus datos.';
        setErrorMessage(typeof detail === 'string' ? detail : JSON.stringify(detail));
      }
    },
  });

  return (
    <div className="flex min-h-[calc(100vh-4rem)] items-center justify-center bg-slate-50 px-4 py-12 sm:px-6 lg:px-8">
      <div className="w-full max-w-md space-y-8 rounded-2xl bg-white p-8 shadow-xl border border-slate-100">
        <div className="text-center">
          <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-xl bg-indigo-600 text-white font-bold text-xl shadow-md">
            FS
          </div>
          <h2 className="mt-4 text-2xl font-bold tracking-tight text-slate-900">
            Iniciar sesión
          </h2>
          <p className="mt-2 text-sm text-slate-500">
            Ingrese sus credenciales para acceder al sistema
          </p>
        </div>

        {errorMessage && (
          <div className="rounded-lg bg-red-50 p-4 border border-red-200">
            <div className="flex">
              <div className="text-sm font-medium text-red-800">
                {errorMessage}
              </div>
            </div>
          </div>
        )}

        <form
          onSubmit={(e) => {
            e.preventDefault();
            e.stopPropagation();
            form.handleSubmit();
          }}
          className="mt-8 space-y-5"
        >
          <form.Field
            name="username"
            validators={{
              onChange: ({ value }) =>
                !value.trim() ? 'El nombre de usuario es obligatorio' : undefined,
            }}
          >
            {(field) => (
              <div>
                <label
                  htmlFor={field.name}
                  className="block text-sm font-medium text-slate-700"
                >
                  Nombre de usuario
                </label>
                <div className="mt-1">
                  <input
                    id={field.name}
                    name={field.name}
                    type="text"
                    value={field.state.value}
                    onBlur={field.handleBlur}
                    onChange={(e) => field.handleChange(e.target.value)}
                    required
                    className="block w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 shadow-sm placeholder:text-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-1 focus:ring-indigo-600 sm:text-sm"
                    placeholder="ej: admin o juan"
                  />
                </div>
                {field.state.meta.errors ? (
                  <p className="mt-1 text-xs text-red-600">
                    {field.state.meta.errors.join(', ')}
                  </p>
                ) : null}
              </div>
            )}
          </form.Field>

          <form.Field
            name="password"
            validators={{
              onChange: ({ value }) =>
                !value ? 'La contraseña es obligatoria' : undefined,
            }}
          >
            {(field) => (
              <div>
                <label
                  htmlFor={field.name}
                  className="block text-sm font-medium text-slate-700"
                >
                  Contraseña
                </label>
                <div className="mt-1">
                  <input
                    id={field.name}
                    name={field.name}
                    type="password"
                    value={field.state.value}
                    onBlur={field.handleBlur}
                    onChange={(e) => field.handleChange(e.target.value)}
                    required
                    className="block w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 shadow-sm placeholder:text-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-1 focus:ring-indigo-600 sm:text-sm"
                    placeholder="••••••••"
                  />
                </div>
                {field.state.meta.errors ? (
                  <p className="mt-1 text-xs text-red-600">
                    {field.state.meta.errors.join(', ')}
                  </p>
                ) : null}
              </div>
            )}
          </form.Field>

          <div>
            <button
              type="submit"
              disabled={isLoading}
              className="flex w-full justify-center rounded-lg bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50 transition"
            >
              {isLoading ? 'Iniciando sesión...' : 'Ingresar'}
            </button>
          </div>
        </form>

        <div className="text-center text-sm text-slate-600">
          ¿No tienes una cuenta?{' '}
          <Link
            to="/register"
            className="font-semibold text-indigo-600 hover:text-indigo-500 hover:underline"
          >
            Regístrate aquí
          </Link>
        </div>

        <div className="rounded-lg bg-slate-50 p-3 text-xs text-slate-500 border border-slate-200">
          <p className="font-semibold text-slate-700 mb-1">Cuentas de prueba:</p>
          <p>• Admin: <span className="font-mono">admin</span> / <span className="font-mono">Admin123!</span></p>
          <p>• Usuario: <span className="font-mono">juan</span> / <span className="font-mono">User1234!</span></p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
