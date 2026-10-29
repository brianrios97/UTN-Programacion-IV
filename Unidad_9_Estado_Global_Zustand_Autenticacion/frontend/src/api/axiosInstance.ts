import axios from 'axios';
import { useAuthStore } from '../store/authStore';

export const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/v1',
  withCredentials: true, // Envía cookies HttpOnly automáticamente en cada petición
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor de respuesta para manejo centralizado del error 401
axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      const url = error.config?.url || '';
      // Si el 401 ocurre en el login o en la comprobación inicial (/auth/me), no forzamos redirección
      const isAuthEndpoint = url.includes('/auth/token') || url.includes('/auth/me');

      if (!isAuthEndpoint) {
        useAuthStore.getState().clearAuth();
        if (window.location.pathname !== '/login') {
          window.location.href = '/login';
        }
      }
    }
    return Promise.reject(error);
  }
);

export default axiosInstance;
