$(document).ready(function(){
    $("#form-registro").validate({
                rules: {
                    codigo: {
                        required: true,
                        minlength: 7,
                        number: true
                    },
                    nombres: "required",
                    apellidos: "required",
                    email: {
                        required: true,
                        email: true
                    },
                    contrasena: {
                        required: true,
                        minlength: 5
                    },
                    cedula : {
                        required: true,
                        number: true
                    }
                },
                messages: {
                    codigo: {
                        required: "El codigo es obligatorio",
                        minlength: "El codigo debe tener 7 caracteres.",
                        number: "EL codigo solo debe contener números"

                    },
                    nombres: "Los nombres es obligatorio",
                    apellidos: "Los apellidos son obligatorios",
                    contrasena: {
                        required: "La contraseña es obligatoria",
                        minlength: "La contraseña debe tener minimo 5 caracteres."
                    },
                    email: "Digite un email valido",
                    cedula: {
                        required: "La cedula es obligatoria",
                        number: "La cedula solo debe contener números"
                    }
                },
                submitHandler: function(form) {
                    form.submit();
                }
                });});