import type { Producto } from '../types/producto';

const API_URL = 'http://localhost:8000/productos';

export const getProductos = async (): Promise<Producto[]> => {
  const response = await fetch(`${API_URL}/`);
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudieron obtener los productos`);
  }
  return response.json();
};

export const getProductoById = async (id: number): Promise<Producto> => {
  const response = await fetch(`${API_URL}/${id}`);
  if (!response.ok) {
    throw new Error(`Error ${response.status}: Producto no encontrado`);
  }
  return response.json();
};

export const createProducto = async (data: {
  nombre: string;
  descripcion: string;
  precio_base: number;
  imagenes_url?: string[];
  disponible?: boolean;
  categoria_ids?: number[];
}): Promise<Producto> => {
  const response = await fetch(`${API_URL}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    const err = await response.json().catch(() => null);
    throw new Error(err?.detail || `Error ${response.status}: No se pudo crear el producto`);
  }
  return response.json();
};

export const updateProducto = async ({
  id,
  data,
}: {
  id: number;
  data: Partial<{
    nombre: string;
    descripcion: string;
    precio_base: number;
    imagenes_url: string[];
    disponible: boolean;
    categoria_ids: number[];
  }>;
}): Promise<Producto> => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    const err = await response.json().catch(() => null);
    throw new Error(err?.detail || `Error ${response.status}: No se pudo actualizar el producto`);
  }
  return response.json();
};

export const deleteProducto = async (id: number): Promise<void> => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo eliminar el producto`);
  }
};
