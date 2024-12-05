# Especificaciones de los casos de uso

## Caso de Uso: UC1 - Registrar usuario
Un usuario no registrado puede registrarse en la aplicación proporcionando
información personal. El usuario solicita registrarse y el sistema pide la información
para el registro. El usuario completa los campos requeridos, como su nombre, la
imagen, dirección de correo electrónico y contraseña. El sistema valida los datos y
crea un usuario si los datos son correctos. Si los datos presentan algún error, dado
que todos los datos son obligatorios y debe de respetarse el formato del correo, la
unicidad del nombre de usuario y validación de contraseña, el sistema niega el registro
y muestra un mensaje de error.

## Caso de Uso: UC2 - Iniciar Sesión
Un usuario registrado puede iniciar sesión en la aplicación proporcionando sus
credenciales. El usuario solicita iniciar sesión y el sistema solicita los datos de inicio
de sesión. El usuario ingresa sus credenciales, que son su dirección de correo
electrónico y contraseña, y estas son verificadas. Si las credenciales son correctas, el
sistema permite el acceso. Si las credenciales son incorrectas, el sistema niega el
inicio de sesión y muestra un mensaje de error.

## Caso de Uso: UC3 - Cerrar Sesión
Un usuario registrado puede cerrar sesión, cuando tenga una sesión abierta.
El usuario solicita cerrar sesión, el sistema registra que el usuario ya no posee sesión
abierta.

## Caso de Uso: UC4 - Recuperar contraseña
Un usuario previamente registrado puede recuperar su contraseña. El usuario
solicita recuperar contraseña, el sistema le solicita un correo electrónico. Si el correo
corresponde con algún correo registrado en el sistema, el sistema enviará un correo
con un hipervínculo donde el usuario al seleccionarlo podrá restablecer su contraseña.

## Caso de Uso: UC5 - Ver perfil
Un usuario previamente registrado puede visualizar los detalles del perfil de un
usuario. El usuario solicita la información del perfil de un usuario, el sistema le muestra
al usuario los datos relacionados a dicho usuario.

## Caso de Uso: UC6 - Editar perfil
Un usuario previamente registrado y que inicio sesión puede editar la
información que se muestra en su perfil. El usuario solicita edición de su perfil. El
sistema le muestra los datos asociados al usuario, que son el nombre, el apellido y la
imagen, y permite al usuario la edición de los mismos. Cuando el usuario termina el
sistema guarda los datos actualizados. Si los datos presentan algún error, dado que
todos los datos son obligatorios y debe de respetarse el formato del correo, el sistema
muestra un mensaje de error y no guarda los datos ingresados.

## Caso de Uso: UC7 - Crear Publicación
Un usuario registrado puede crear una nueva publicación. El usuario solicita
crear una publicación y el sistema pide la información sobre la publicación. El usuario
completa los detalles de la publicación como: el título, la imagen y el contenido. Si los
datos son correctos el sistema crea la publicación. Si los datos presentan algún error,
dado que todos los datos son obligatorios, el sistema muestra un mensaje de error y
no guarda los datos ingresados.

## Caso de Uso: UC8 - Listar publicaciones
Tanto un usuario registrado como no registrado puede solicitar las
publicaciones en la plataforma. El sistema muestra las publicaciones de forma
paginada. El usuario podrá ir pasando de página para poder ver todas las
publicaciones. En caso de no encontrar publicaciones se mostrará únicamente el
botón de crear publicación.

## Caso de Uso: UC9 - Editar publicación
El usuario previamente registrado puede editar el contenido de una publicación
creada por él. El usuario solicita la edición de una publicación, el sistema busca la
información de la publicación y la muestra al usuario. Al finalizar la edición, el sistema
guarda los datos asociados con la publicación. Si los datos presentan algún error,
dado que todos los datos son obligatorios, el sistema muestra un mensaje de error y
no guarda los datos ingresados.

## Caso de Uso: UC10 - Crear comentario
Un usuario registrado puede crear un comentario en una publicación existente.
El usuario solicita la creación de un comentario, el sistema pide los datos para la
creación del comentario. El usuario ingresa el texto o contenido que desea agregar en
el comentario. Si el campo de texto presenta algún error, dado que es obligatorio, el
sistema muestra un mensaje de error y no guarda los datos ingresados.

## Caso de Uso: UC11 - Listar comentarios
El usuario puede ver los comentarios de una publicación. El usuario solicita los
comentarios de una publicación y el sistema muestra los comentarios asociados a la
publicación. En caso de no haber comentario, no se listará ninguno, mostrando
únicamente el campo de comentar.

## Caso de Uso: UC12 - Editar comentario
Un usuario registrado puede actualizar un comentario que haya creado en una
publicación existente. El usuario solicita la edición de un comentario, el sistema busca
y muestra los datos para la edición del comentario. El usuario actualiza la información,
el sistema los valida y guarda. Si el campo de texto presenta algún error, dado que es
obligatorio, el sistema muestra un mensaje de error y no guarda los datos ingresados.

## Caso de Uso: UC13 - Eliminar comentario
Un usuario registrado puede eliminar un comentario que haya creado en una
publicación existente. El usuario solicita eliminar un comentario. El sistema solicita la
aprobación del usuario para eliminar. En caso de aceptar, el sistema elimina el
comentario, de lo contrario no se hace la eliminación.

## Caso de Uso: UC14 - Ver publicación
Un usuario puede ver los detalles de una publicación específica. El usuario
solicita los detalles de una publicación. El sistema muestra los datos asociados a la
publicación.

## Caso de Uso: UC15 - Visualizar estadísticas
Un usuario administrador, puede visualizar un conjunto de estadísticas. El
usuario administrador solicita visualizar estadísticas. El sistema muestra las siguientes
estadísticas: cantidad de usuarios, cantidad de publicaciones, cantidad de
comentarios en la aplicación, promedio de publicaciones por usuario, usuario con más
publicaciones y cuantas publicaciones tiene, usuario con más comentarios y cuantos
comentarios son. En caso de que algún campo de las estadísticas no tenga datos
asociados, el sistema mostrará un 0.

## Caso de Uso: UC16 - Ver usuario
Un usuario administrador puede ver la información de un usuario. El usuario
administrador solicita ver información sobre otro usuario. El sistema muestra los datos
asociados al usuario. En caso de no existir usuario el sistema muestra un error.

## Caso de Uso: UC17 - Editar usuario
Un usuario administrador puede editar la información de un usuario. El usuario
solicita la edición del usuario. El sistema muestra la información asociada para la
edición, que son el nombre, el apellido, la imagen y el correo electrónico. El usuario
edita la información necesaria, el sistema valida los datos y guarda los datos
asociados al usuario. Si los datos presentan algún error, dado que todos los datos son
obligatorios y debe de respetarse el formato del correo, la unicidad del nombre de
usuario y validación de contraseña, el sistema niega el registro y muestra un mensaje
de error.

## Caso de Uso: UC18 - Bloquear usuario
Un usuario administrador, puede restringir el acceso a un usuario. Un usuario
administrador solicita el bloqueo de otro usuario. El sistema solicita la confirmación
del bloqueo. En caso de aceptar, el sistema bloquea el acceso del usuario, de lo
contrario el sistema no bloquea el acceso del usuario.

## Caso de Uso: UC19 - Eliminar usuario
Un usuario administrador, puede eliminar un usuario. El usuario administrador
solicita la eliminación de otro usuario. El sistema solicita la confirmación de la
eliminación. En caso de aceptar, el sistema elimina el usuario seleccionado, de lo
contrario el sistema no elimina el usuario seleccionado.

## Caso de Uso: UC20 - Bloquear publicación
Un usuario administrador puede bloquear la visibilidad de una publicación. Un
usuario administrador solicita el bloqueo de una publicación. El sistema solicita la
confirmación del bloqueo. En caso de aceptar, el sistema bloquea la visibilidad de una
publicación al público en general, de lo contrario el sistema no bloquea la publicación.

## Caso de Uso: UC21 - Eliminar publicación
Un usuario administrador puede eliminar una publicación. El usuario
administrador solicita la eliminación de una publicación. El sistema solicita la
confirmación de la eliminación. En caso de aceptar, el sistema elimina la publicación
seleccionada, de lo contrario el sistema no elimina la publicación.

## Caso de Uso: UC22 - Buscar usuarios
Un usuario administrador puede buscar usuarios. El sistema muestra los usuarios de forma
paginada. El usuario administrador podrá ir pasando de página para poder ver todos los
usuarios. En caso de no encontrar usuarios se mostrará un mensaje que indique esto.