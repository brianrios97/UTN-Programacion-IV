export interface UsuarioAuth {
  id: number;
  username: string;
  full_name: string;
  email: string;
  role: 'admin' | 'user' | string;
  disabled: boolean;
}

export type UserPublic = UsuarioAuth;

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  full_name: string;
  email: string;
  password: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface MessageResponse {
  mensaje: string;
}
