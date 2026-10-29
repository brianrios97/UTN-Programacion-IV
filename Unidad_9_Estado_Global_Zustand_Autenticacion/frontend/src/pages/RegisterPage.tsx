import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useForm } from '@tanstack/react-form';
import { axiosInstance } from '../api/axiosInstance';
import type { RegisterData, UserPublic } from '../types/auth.types';

export const RegisterPage: React.FC = () => {
  const navigate = useNavigate();
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const form = useForm({
    defaultValues: {
      username: '',
      full_name: '',
      email: '',
      password: '',
    } as RegisterData,
    onSubmit: async ({ value }) => {
      setErrorMessage(null);
      setIsSubmitting(true);
      try {
        await axiosInstance.post<UserPublic>('/auth/register', value);
        // Al completar exitosamente, redirige a /login (HU-01)
        navigate('/login', {
          state: { message: '¡Cuenta creada con éxito! Ya puedes iniciar sesión.' },
        });
      } catch (err: any) {
        setIsSubmitting(false);
        const detail =
          err.response?.data?.detail ||
          err.message ||
          'Error al registrarse. Verifique los datos ingresados.';
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
            Crear nueva cuenta
          </h2>
          <p className="mt-2 text-sm text-slate-500">
            Regístrate para comenzar a usar la plataforma
          </p>
        </div>

        {errorMessage && (
          <div className="rounded-lg bg-red-50 p-4 border border-red-200">
            <div className="text-sm font-medium text-red-800">{errorMessage}</div>
          </div>
        )}

        <form
          onSubmit={(e) => {
            e.preventDefault();
            e.stopPropagation();
            form.handleSubmit();
          }}
          className="mt-6 space-y-4"
        >
          <form.Field
            name="username"
            validators={{
              onChange: ({ value }) =>
                value.length < 3
                  ? 'El nombre de usuario debe tener al menos 3 caracteres'
                  : undefined,
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
                    placeholder="usuario123"
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
            name="full_name"
            validators={{
              onChange: ({ value }) =>
                !value.trim() ? 'El nombre completo es obligatorio' : undefined,
            }}
          >
            {(field) => (
              <div>
                <label
                  htmlFor={field.name}
                  className="block text-sm font-medium text-slate-700"
                >
                  Nombre completo
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
                    placeholder="Juan Pérez"
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
            name="email"
            validators={{
              onChange: ({ value }) =>
                !value.includes('@') ? 'Ingrese un email válido' : undefined,
            }}
          >
            {(field) => (
              <div>
                <label
                  htmlFor={field.name}
                  className="block text-sm font-medium text-slate-700"
                >
                  Correo electrónico
                </label>
                <div className="mt-1">
                  <input
                    id={field.name}
                    name={field.name}
                    type="email"
                    value={field.state.value}
                    onBlur={field.handleBlur}
                    onChange={(e) => field.handleChange(e.target.value)}
                    required
                    className="block w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-900 shadow-sm placeholder:text-slate-400 focus:border-indigo-600 focus:outline-none focus:ring-1 focus:ring-indigo-600 sm:text-sm"
                    placeholder="juan@ejemplo.com"
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
                value.length < 8
                  ? 'La contraseña debe tener al menos 8 caracteres'
                  : undefined,
            }}
          >
            {(field) => (
              <div>
                <label
                  htmlFor={field.name}
                  className="block text-sm font-medium text-slate-700"
                >
                  Contraseña (mínimo 8 caracteres)
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

          <div className="pt-2">
            <button
              type="submit"
              disabled={isSubmitting}
              className="flex w-full justify-center rounded-lg bg-indigo-600 px-4 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600 disabled:opacity-50 transition"
            >
              {isSubmitting ? 'Registrando...' : 'Registrarse'}
            </button>
          </div>
        </form>

        <div className="text-center text-sm text-slate-600">
          ¿Ya tienes cuenta?{' '}
          <Link
            to="/login"
            className="font-semibold text-indigo-600 hover:text-indigo-500 hover:underline"
          >
            Inicia sesión aquí
          </Link>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;
