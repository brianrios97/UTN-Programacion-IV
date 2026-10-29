import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import { axiosInstance } from '../api/axiosInstance';
import type { UsuarioAuth, LoginCredentials } from '../types/auth.types';

interface AuthState {
  user: UsuarioAuth | null;
  isLoading: boolean;
  error: string | null;
  login: (credentials: LoginCredentials) => Promise<void>;
  logout: () => Promise<void>;
  checkSession: () => Promise<void>;
  clearAuth: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      isLoading: false,
      error: null,

      login: async ({ username, password }: LoginCredentials) => {
        set({ isLoading: true, error: null });
        try {
          // 1. Enviar credenciales como formulario OAuth2 urlencoded
          const formData = new URLSearchParams();
          formData.append('username', username);
          formData.append('password', password);

          await axiosInstance.post('/auth/token', formData, {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
          });

          // 2. Obtener los datos del usuario autenticado vía /auth/me
          const meResponse = await axiosInstance.get<UsuarioAuth>('/auth/me');
          set({ user: meResponse.data, isLoading: false, error: null });
        } catch (err: any) {
          const detail =
            err.response?.data?.detail ||
            err.message ||
            'Error al iniciar sesión. Verifique sus credenciales.';
          set({ error: typeof detail === 'string' ? detail : JSON.stringify(detail), isLoading: false });
          throw err;
        }
      },

      logout: async () => {
        set({ isLoading: true });
        try {
          await axiosInstance.post('/auth/logout');
        } catch (err) {
          console.error('Error al cerrar sesión en el servidor:', err);
        } finally {
          set({ user: null, isLoading: false, error: null });
        }
      },

      checkSession: async () => {
        set({ isLoading: true });
        try {
          const response = await axiosInstance.get<UsuarioAuth>('/auth/me');
          set({ user: response.data, isLoading: false, error: null });
        } catch {
          // Si el token expiró o no existe cookie válida, se limpia la sesión
          set({ user: null, isLoading: false });
        }
      },

      clearAuth: () => {
        set({ user: null, error: null, isLoading: false });
      },
    }),
    {
      name: 'auth-storage',
      storage: createJSONStorage(() => sessionStorage),
      // Guardar solo los datos del usuario, NUNCA tokens (RN-03, RN-13)
      partialize: (state) => ({ user: state.user }),
    }
  )
);
