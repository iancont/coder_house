# Nombre del Proyecto: CRM ++ en Django

**Comisión:** 54140

**Alumno:** Ian Contreras

## Explicación breve del proyecto en cuanto al servicio
CRM ++ en Django es un sistema de gestión de relaciones con clientes (CRM) diseñado para ayudar a las empresas a gestionar sus interacciones con clientes actuales y potenciales. El sistema permite a los usuarios almacenar y organizar información de contacto y seguimiento de interacciones.

## Explicación breve técnica: URLs, modelos, plantillas
Es una aplicación monolítica en Django, donde tenemos tres modelos principales: Record, SalesMember y Lead.

- **Record:** Maneja todos los contactos que se ingresan en la base de datos, incluyendo información de contacto y de creación. Tiene funcionalidades CRUD en la aplicación web.
- **SalesMember:** Representa a los agentes de ventas que utilizan el CRM. El CRUD de estos solo está disponible en el panel de administración.
- **Lead:** Permite manejar a los contactos en sus distintas etapas del proceso de venta. Tiene funcionalidades CRUD en el panel de administración.

## Mejoras futuras
Mejorar la parte front-end con React o incluir un dashboard con analíticas de Power BI o Tableau sería la mejor forma de extraer insights de los datos.

## Problemas conocidos
Poca escalabilidad al ser un monolito y tener los templates HTML en Django. Crear una API para la lógica de negocio y trabajar la parte front-end en React sería lo más adecuado.
