import type { Ingrediente } from '../types/ingrediente';

const API_URL = 'http://localhost:8000/ingredientes';

export const getIngredientes = async (): Promise<Ingrediente[]> => {
  const response = await fetch(`${API_URL}/`);
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudieron obtener los ingredientes`);
  }
  return response.json();
};

export const getIngredienteById = async (id: number): Promise<Ingrediente> => {
  const response = await fetch(`${API_URL}/${id}`);
  if (!response.ok) {
    throw new Error(`Error ${response.status}: Ingrediente no encontrado`);
  }
  return response.json();
};

export const createIngrediente = async (data: Omit<Ingrediente, 'id'>): Promise<Ingrediente> => {
  const response = await fetch(`${API_URL}/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (response.status === 409) {
    const err = await response.json();
    throw new Error(err.detail || 'Ya existe un ingrediente con ese nombre');
  }
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo crear el ingrediente`);
  }
  return response.json();
};

export const updateIngrediente = async ({
  id,
  data,
}: {
  id: number;
  data: Partial<Omit<Ingrediente, 'id'>>;
}): Promise<Ingrediente> => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (response.status === 409) {
    const err = await response.json();
    throw new Error(err.detail || 'Ya existe otro ingrediente con ese nombre');
  }
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo actualizar el ingrediente`);
  }
  return response.json();
};

export const deleteIngrediente = async (id: number): Promise<void> => {
  const response = await fetch(`${API_URL}/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error(`Error ${response.status}: No se pudo eliminar el ingrediente`);
  }
};
