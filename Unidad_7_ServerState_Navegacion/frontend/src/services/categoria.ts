import type { Categoria } from '../types/categoria';

const API_URL = 'http://localhost:8000/categorias';

export const getCategorias = async (): Promise<Categoria[]> => {
  const response = await fetch(`${API_URL}/`);
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudieron obtener las categorias`);
  }
  return response.json();
};

export const getCategoriaById = async (id: number): Promise<Categoria> => {
  const response = await fetch(`${API_URL}/${id}`);
  if (!response.ok) {
    throw new Error(`Error ${response.status}: Categoria no encontrada`);
  }
  return response.json();
};

export const createCategoria = async (data: Omit<Categoria, 'id'>): Promise<Categoria> => {
  const response = await fetch(`${API_URL}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (response.status === 409) {
    const err = await response.json();
    throw new Error(err.detail || 'Ya existe una categoria con ese nombre');
  }
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo crear la categoria`);
  }
  return response.json();
};

export const updateCategoria = async ({
  id,
  data,
}: {
  id: number;
  data: Partial<Omit<Categoria, 'id'>>;
}): Promise<Categoria> => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (response.status === 409) {
    const err = await response.json();
    throw new Error(err.detail || 'Ya existe otra categoria con ese nombre');
  }
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo actualizar la categoria`);
  }
  return response.json();
};

export const deleteCategoria = async (id: number): Promise<void> => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo eliminar la categoria`);
  }
};
