# Comparación y Evaluación de cinco Frameworks Web de Backend

## Descripción Aplicación
Aplicación que permite a los usuarios registrarse, iniciar sesión, publicar contenido y comentarlo. También permite a los administradores gestionar estadísticas, modificar información, censurar información no permitida y bloquear usuarios.

## Implementación
Aplicación web del tipo MPA implementada en 5 framework de backend distintos:
- Django: https://github.com/danielviei/tesis-django-app
- ASP .NET CORE: https://github.com/danielviei/NetCoreApp
- Laravel: https://github.com/Eduhuu/laravel-app
- Express JS: https://github.com/Eduhuu/express-pug-app
- Ruby on Rails: https://github.com/Eduhuu/ruby-on-rail-app

## Motivación
Esta aplicación permitirá evaluar las capacidades de los frameworks seleccionados en cuanto a la presentación de datos, paginación, operaciones CRUD (Crear, Leer, Actualizar, Eliminar), y manejo de relaciones entre modelos.

- Las publicaciones con comentarios permitirán evaluar las operaciones CRUD, paginación y las relaciones entre modelos.
- Las parte administrativa permitirá evaluar la gestión de estadísticas, modificación de información, bloqueo de usuarios, y las capacidades de autenticación y autorización.
- Las recuperación de contraseña permitirá evaluar la validación por correo electrónico y el proceso de restauración de contraseña.

## Metodología
La aplicación esta requisitada y diseñada usando la metodología UP. Al ser una metodología dirigida por casos de uso, se podrá realizar una traza desde los requisitos, hasta el código implementado en cada framework. Esta trazabiliad permite verificar la transformación de los requisitos en elementos de modelo sucesores, resultantes del análisis y diseño, implementación, pruebas y despliegue. De esta manera se podrá comparar cada framework y las aplicaciones resultantes de manera más efectiva.

| <img src="img/trazabilidadCasosUsoDisciplinas.png" width=80% style="background-color:white;"><br><sub>Trazabilidad de Requisitos por disciplinas</sub> |
| :---: |

## Modelo de Casos de uso

### Usuario no registrado
![modelo caso de uso usuario no registrado](scenariosView/usecaseModel/useCaseDiagramAnonymous/baseApp.svg)

### Usuario registrado
![modelo caso de uso usuario registrado](scenariosView/usecaseModel/useCaseDiagramUser/baseApp.svg)

### Usuario administrador
![modelo caso de uso usuario administrador](scenariosView/usecaseModel/useCaseDiagramAdmin/baseApp.svg)

### Especificaciones de casos de uso
La descripción de cada caso de uso lo podrá ver en: [especificaciones de los casos de uso](scenariosView/usecaseModel/useCaseSpecifications.md)

### Prototipo de pantallas
Los prototipos de las pantallas las podrá ver en: [prototipo de pantallas](scenariosView/usecaseModel/prototype/prototype.md)

### Trazabilidad entre pantallas y casos de uso
| <img src="scenariosView/usecaseModel/prototypeUseCaseTrace/prototypeTrace.svg" width=80% style="background-color:white;"> |
| :---: |

## Modelo de Análisis

### Diagrama de clases de análisis
#### Usuario no registrado
![diagrama de clases de análisis usuario no registrado](logicalView/analisysView/classAnalisys/analysisClassDiagramRegisterNoUser/analysisClassDiagramRegisterNoUser.svg)

#### Usuario registrado
![diagrama de clases de análisis usuario registrado](logicalView/analisysView/classAnalisys/analysisClassDiagramRegisterUser/analysisClassDiagramRegisterUser.svg)

#### Usuario administrador
![diagrama de clases de análisis usuario administrador](logicalView/analisysView/classAnalisys/analysisClassDiagramAdminUser/analysisClassDiagramAdminUser.svg)

### Arquitectura de análisis
![arquitectura de análisis](logicalView/analisysView/architectureAnalisys/analysisPackageDiagram/analysisPackageDiagram.svg)

### Realización de análisis de casos de uso OJO

#### Diagrama de clases de análisis de UC7 – Crear Publicación
![Diagrama de clases de análisis de UC7](logicalView/analisysView/usecaseAnalisys/analysisClassDiagramUC7/analysisClassDiagramUC7.svg)

#### Diagrama de colaboración de análisis de UC7 – Crear Publicación
![Diagrama de colaboración de análisis de UC7](logicalView/analisysView/usecaseAnalisys/analysisComunicationDiagramUC7/analysisComunicationDiagramUC7.svg)

## Modelo de Diseño Framework Express

### Arquitectura de Sistema
![arquitectura de sistema de Framework Express](logicalView/designView/express/architectureDesign/componentDiagram/architecture_design.svg)