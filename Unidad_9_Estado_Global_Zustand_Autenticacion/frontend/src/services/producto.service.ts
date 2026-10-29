import { axiosInstance } from '../api/axiosInstance';
import type { Producto } from '../types/producto';

export interface CreateProductoPayload {
  nombre: string;
  descripcion: string;
  precio_base: number;
  imagenes_url?: string[];
  disponible?: boolean;
  categoria_ids?: number[];
}

export const getProductos = async (): Promise<Producto[]> => {
  const response = await axiosInstance.get<Producto[]>('/productos/');
  return response.data;
};

export const getProductoById = async (id: number): Promise<Producto> => {
  const response = await axiosInstance.get<Producto>(`/productos/${id}`);
  return response.data;
};

export const createProducto = async (
  data: CreateProductoPayload
): Promise<Producto> => {
  const response = await axiosInstance.post<Producto>('/productos/', data);
  return response.data;
};

export const updateProducto = async ({
  id,
  data,
}: {
  id: number;
  data: Partial<CreateProductoPayload>;
}): Promise<Producto> => {
  const response = await axiosInstance.put<Producto>(`/productos/${id}`, data);
  return response.data;
};

export const deleteProducto = async (id: number): Promise<void> => {
  await axiosInstance.delete(`/productos/${id}`);
};
