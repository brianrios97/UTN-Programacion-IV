import React from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { axiosInstance } from '../api/axiosInstance';
import type { UsuarioAuth } from '../types/auth.types';

export const AdminUsersPage: React.FC = () => {
  const queryClient = useQueryClient();

  // Consulta de usuarios registrados
  const { data: usuarios, isLoading, isError, error } = useQuery<UsuarioAuth[]>({
    queryKey: ['admin-usuarios'],
    queryFn: async () => {
      const response = await axiosInstance.get<UsuarioAuth[]>('/admin/usuarios');
      return response.data;
    },
  });

  // Mutación para desactivar usuario
  const desactivarMutation = useMutation({
    mutationFn: async (id: number) => {
      const response = await axiosInstance.post<UsuarioAuth>(`/admin/usuarios/${id}/desactivar`);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin-usuarios'] });
    },
  });

  // Mutación para activar usuario
  const activarMutation = useMutation({
    mutationFn: async (id: number) => {
      const response = await axiosInstance.post<UsuarioAuth>(`/admin/usuarios/${id}/activar`);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin-usuarios'] });
    },
  });

  if (isLoading) {
    return (
      <div className="flex min-h-[50vh] items-center justify-center">
        <div className="flex flex-col items-center gap-2">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-indigo-600 border-t-transparent"></div>
          <p className="text-sm text-slate-500">Cargando usuarios...</p>
        </div>
      </div>
    );
  }

  if (isError) {
    return (
      <div className="mx-auto max-w-7xl px-4 py-8">
        <div className="rounded-lg bg-red-50 p-4 border border-red-200">
          <p className="text-sm font-medium text-red-800">
            Error al cargar usuarios: {(error as Error).message}
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <div className="sm:flex sm:items-center sm:justify-between mb-8">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
            Gestión de Usuarios
          </h1>
          <p className="mt-2 text-sm text-slate-500">
            Panel de administración para supervisar usuarios y aplicar borrado lógico (activar/desactivar cuentas).
          </p>
        </div>
      </div>

      <div className="overflow-hidden rounded-xl border border-slate-200 bg-white shadow-sm">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-slate-200">
            <thead className="bg-slate-50">
              <tr>
                <th scope="col" className="px-6 py-3.5 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  ID
                </th>
                <th scope="col" className="px-6 py-3.5 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  Usuario
                </th>
                <th scope="col" className="px-6 py-3.5 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  Nombre Completo
                </th>
                <th scope="col" className="px-6 py-3.5 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  Email
                </th>
                <th scope="col" className="px-6 py-3.5 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  Rol
                </th>
                <th scope="col" className="px-6 py-3.5 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  Estado
                </th>
                <th scope="col" className="px-6 py-3.5 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider">
                  Acciones
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200 bg-white">
              {usuarios && usuarios.length > 0 ? (
                usuarios.map((u) => (
                  <tr key={u.id} className="hover:bg-slate-50 transition-colors">
                    <td className="whitespace-nowrap px-6 py-4 text-sm font-mono text-slate-500">
                      #{u.id}
                    </td>
                    <td className="whitespace-nowrap px-6 py-4 text-sm font-semibold text-slate-900">
                      {u.username}
                    </td>
                    <td className="whitespace-nowrap px-6 py-4 text-sm text-slate-600">
                      {u.full_name}
                    </td>
                    <td className="whitespace-nowrap px-6 py-4 text-sm text-slate-500">
                      {u.email}
                    </td>
                    <td className="whitespace-nowrap px-6 py-4 text-sm">
                      <span
                        className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-bold uppercase tracking-wider ${
                          u.role === 'admin'
                            ? 'bg-amber-100 text-amber-800 border border-amber-200'
                            : 'bg-indigo-100 text-indigo-800 border border-indigo-200'
                        }`}
                      >
                        {u.role}
                      </span>
                    </td>
                    <td className="whitespace-nowrap px-6 py-4 text-sm">
                      {u.disabled ? (
                        <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-red-100 text-red-800 border border-red-200">
                          Inactivo (Desactivado)
                        </span>
                      ) : (
                        <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800 border border-emerald-200">
                          Activo
                        </span>
                      )}
                    </td>
                    <td className="whitespace-nowrap px-6 py-4 text-right text-sm font-medium">
                      {u.disabled ? (
                        <button
                          onClick={() => activarMutation.mutate(u.id)}
                          disabled={activarMutation.isPending}
                          className="inline-flex items-center rounded-lg bg-emerald-600 px-3 py-1.5 text-xs font-semibold text-white shadow-sm hover:bg-emerald-500 disabled:opacity-50 transition"
                        >
                          Activar
                        </button>
                      ) : (
                        <button
                          onClick={() => desactivarMutation.mutate(u.id)}
                          disabled={desactivarMutation.isPending}
                          className="inline-flex items-center rounded-lg bg-amber-600 px-3 py-1.5 text-xs font-semibold text-white shadow-sm hover:bg-amber-500 disabled:opacity-50 transition"
                        >
                          Desactivar
                        </button>
                      )}
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={7} className="px-6 py-8 text-center text-sm text-slate-500">
                    No hay usuarios registrados en el sistema.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default AdminUsersPage;
