# Frontend ? FoodStore UI (Unidad 7)

**Materia:** Programaci?n IV  
**Tecnicatura Universitaria en Programaci?n a Distancia ? UTN**  
**Estudiante:** Brian Emanuel Rios  

Frontend desarrollado con **React 19**, **TypeScript**, **Vite**, **Tailwind CSS v4**, **TanStack Query v5** y **React Router v7**.

---

## ?? Aspectos Implementados
1. **Server State con TanStack Query:**
   - `useQuery`: Obtiene el listado de categor?as (`queryKey: ['categorias']`), manejando estados de carga (`isLoading`), error (`isError`) y reintentos.
   - `useMutation`: Operaciones de alta (`createCategoria`), edici?n (`updateCategoria`) y baja (`deleteCategoria`).
   - `queryClient.invalidateQueries`: Invalida autom?ticamente la cach? tras cada mutaci?n exitosa, manteniendo los datos siempre actualizados con el backend.
2. **Estado Local con `useState`:**
   - `useState` reservado exclusivamente para la interfaz de usuario: apertura/cierre del modal (`isModalOpen`) y categor?a seleccionada para edici?n (`categoriaEditar`).
3. **Navegaci?n con React Router:**
   - Barra de navegaci?n (`Navbar.tsx`) con enlaces `NavLink` a `/categorias` y `/productos`.
   - Redirecci?n autom?tica de `/` a `/categorias`.
4. **Dise?o y Est?tica con Tailwind CSS:**
   - Paleta moderna en modo oscuro (fondos oscuros, acentos en esmeralda/teal y alertas en rose).
   - Componentes modulares y reutilizables en `src/components/`.
5. **Tipado Estricto TypeScript:**
   - Interfaces `Categoria` y `Producto` centralizadas en `src/types/`.
   - Props estrictamente tipados en todos los componentes. Cero uso de `any`.

---

## ?? Comandos
```bash
# Instalar dependencias
npm install

# Iniciar en modo desarrollo
npm run dev

# Compilar para producci?n (validaci?n de tipos TypeScript)
npm run build
```
