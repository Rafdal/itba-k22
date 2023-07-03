
# Materia Créditos Créditos requeridos Correlativas

# Atributos de las materias:
#  "code": 'XX.XX',
#  "name": "Nombre de la materia",
#  "creds": 6,
#  "corr": ['XX.XX', 'XX.XX']
#  "min_creds": 144,

planK22 = [
    {
        "year": 1, 
        "period": 1,
        "subjects": [
            {"code": '12.67', "name": "Química General", "creds": 6},
            {"code": '71.93', "name": "Principios de Informática", "creds": 3},
            {"code": '92.01', "name": "Análisis Matemático I", "creds": 6},
            {"code": '93.18', "name": "Álgebra Lineal", "creds": 6},
            {"code": '94.33', "name": "Tecnología y Sociedad", "creds": 3},
        ]
    },
    {
        "year": 1, 
        "period": 2,
        "subjects": [
            {"code": '25.01', "name": "Fundamentos de Electrónica",	"creds": 3, "corr": ['71.93']},
            {"code": '25.02', "name": "Programación I", "creds": 6, "corr": ['71.93']},
            {"code": '31.08', "name": "Sistemas de Representación", "creds": 3,},
            {"code": '92.02', "name": "Análisis Matemático II", "creds": 6, "corr": ['92.01', '93.18']},
            {"code": '93.41', "name": "Física I", "creds": 6, "corr": ['92.01']},
        ]
    },
    {
        "year": 2, 
        "period": 1,
        "subjects": [
            {"code": '25.03', "name": "Algoritmos y Estructuras de Datos", "creds": 3, "corr": ['25.02']},
            {"code": '92.03', "name": "Análisis Matemático III", "creds": 6, "corr": ['92.01', '93.18']},
            {"code": '93.16', "name": "Matemática Discreta", "creds": 3, "corr": ['93.18']},
            {"code": '93.24', "name": "Probabilidad y Estadística", "creds": 6, "corr": ['92.02']},
            {"code": '93.42', "name": "Física II", "creds": 6, "corr": ['92.02']},
        ]
    },
    {
        "year": 2, 
        "period": 2,
        "subjects": [
            {"code": '16.55', "name": "Biología", "creds": 3,},
            {"code": '25.10', "name": "Teoría de Circuitos 1", "creds": 6, "corr": ['92.03', '25.01']},
            {"code": '92.04', "name": "Análisis Matemàtico IV", "creds": 6, "corr": ['92.02', '92.03']},
            {"code": '93.07', "name": "Métodos Numéricos", "creds": 3, "corr": ['92.03', '93.24']},
            {"code": '93.43', "name": "Física III", "creds": 6, "corr": ['92.03', '93.41']},
        ]
    },
    {
        "year": 3, 
        "period": 1,
        "subjects": [
            {"code": '25.12', "name": "Tecnología de Materiales Electrónicos", "creds": 4, "corr": ['93.42', '25.10']},
            {"code": '25.13', "name": "Laboratorio de Electrónica 1", "creds": 6, "corr": ['25.10']},
            {"code": '25.18', "name": "Física Electrónica", "creds": 3, "corr": ['92.04', '25.10']},
            {"code": '92.07', "name": "Análisis Matemático V", "creds": 4, "corr": ['92.04']},
            {"code": '93.61', "name": "Física IV", "creds": 4, "corr": ['93.42', '93.43']},
            {"code": '94.43', "name": "Metodología del Diseño", "creds": 3, "corr": ['93.24']},
        ]
    },
    {
        "year": 3, 
        "period": 2,
        "subjects": [
            {"code": '25.14', "name": "Teoría de Circuitos 2", "creds": 6, "corr": ['25.10', '25.12']},
            {"code": '25.15', "name": "Electrónica I", "creds": 6, "corr": ['25.18']},
            {"code": '25.16', "name": "Laboratorio de Electrónica 2", "creds": 3, "corr": ['25.13']},
            {"code": '25.17', "name": "Electrónica II", "creds": 6, "corr": ['25.13']},
            {"code": '94.44', "name": "Proyecto Interdisciplinario", "creds": 3, "corr": ['94.43']},
            {"code": '94.51', "name": "Inglés I"},
        ]
    },
    {
        "year": 4, 
        "period": 1,
        "subjects": [
            {"code": '25.20', "name": "Análisis de Señales y Sistemas Digitales", "creds": 6, "corr": ['25.14']},
            {"code": '25.21', "name": "Electrónica III", "creds": 4, "corr": ['25.15']},
            {"code": '25.22', "name": "Electromagnetismo", "creds": 4, "corr": ['93.43', '92.07']},
            {"code": '25.23', "name": "Sistemas de Control", "creds": 6, "corr": ['92.07']},
            {"code": '25.24', "name": "Laboratorio de Electrónica 3", "creds": 4, "corr": ['25.16']},
        ]},
    {
        "year": 4, 
        "period": 2,
        "subjects": [
            {"code": '11.15', "name": "Organización Industrial", "creds": 3, "corr": ['93.24']},
            {"code": '25.26', "name": "Transmisión de la Información", "creds": 6, "corr": ['25.22', '25.20']},
            {"code": '25.27', "name": "Sistemas Embebidos", "creds": 6, "corr": ['25.17',  '25.16', '25.20']},
            {"code": '25.28', "name": "Electrónica IV", "creds": 4, "corr": ['25.24', '25.23', '25.12']},
            {"code": '61.27', "name": "Análisis de Coyuntura Económica", "creds": 3, "corr": ['93.24']},
        ],
    },
    {
        "year": 5, 
        "period": 1,
        "subjects": [
            {"code": '12.83', "name": "Seguridad Ocupacional y Ambiental", "creds": 3, "min_creds": 120},
            {"code": '25.30', "name": "Electrónica V", "creds": 4, "corr": ['25.27']},
            {"code": '25.31', "name": "Proyectos Electrónicos", "creds": 4, "min_creds": 168},
            {"code": '25.32', "name": "Proyecto Integrador (anual)", "creds": 6, "min_creds": 168},
            {"code": '61.16', "name": "Introducción a las Finanzas", "creds": 3, "corr": ['11.15', '61.27']},
        ]
    },
    {
        "year": 5, 
        "period": 2,
        "subjects": [
            {"code": '61.31', "name": "Derecho para Ingenieros", "creds": 3, "min_creds": 144},
            {"code": '94.52', "name": "Inglés II",	"corr": ['94.51']},
            {"code": '94.65', "name": "Practica Profesional supervisada", "min_creds": 144},
        ]
    },
]

electivasK22 = [
	{"code": '10.09', "name": "Formación para Emprendedores", "creds": 3, "min_creds": 96,},
	{"code": '16.04', "name": "Neurociencias y Desarrollo Productivo", "creds": 3, "min_creds": 96,},
	{"code": '22.22', "name": "Antenas y Radiopropagacion", "creds": 6,},
	{"code": '22.29', "name": "Microondas", "creds": 6,},
	{"code": '22.46', "name": "Procesamiento Adaptativo de Señales", "creds": 6,},
	{"code": '22.47', "name": "Procesamiento de Voz", "creds": 3,},
	{"code": '22.48', "name": "Procesamiento de Imágenes", "creds": 3,},
	{"code": '22.64', "name": "Comunicaciones Digitales", "creds": 6,},
	{"code": '22.66', "name": "Redes Digitales", "creds": 6,},
	{"code": '22.88', "name": "Sensores y Actuadores", "creds": 6,},
	{"code": '22.90', "name": "Automación Industrial", "creds": 6,},
	{"code": '22.93', "name": "Control Automático", "creds": 6,},
	{"code": '23.10', "name": "Formación General II", "creds": 3,},
	{"code": '23.12', "name": "Introducción a la Investigación", "creds": 3,},
	{"code": '23.18', "name": "Electrónica e Instrumentación", "creds": 6,},
	{"code": '25.51', "name": "Electrónica aplicada a Movilidad Eléctrica", "creds": 4, "min_creds": 96,},
	{"code": '25.52', "name": "Electrónica de Potencia", "creds": 4, "corr": [25.28,]},
	{"code": '25.53', "name": "Señales Aleatorias", "creds": 4, "corr": [25.26,]},
	{"code": '25.55', "name": "Microelectrónica", "creds": 3, "corr": [25.17, 25.15,]},
	{"code": '25.56', "name": "Diseño Físico de Circuitos Integrados", "creds": 3, "corr": [25.55,]},
	{"code": '25.57', "name": "Diseño Analógico de Circuitos Integrados (Anual)", "creds": 6, "corr": [25.56,]},
	{"code": '25.59', "name": "Dispositivos Lógicos Programables", "creds": 3, "corr": [25.56,]},
	{"code": '25.60', "name": "Control Avanzado", "creds": 3, "corr": [25.23,]},
	{"code": '25.61', "name": "Tecnologías para el agro", "creds": 3, "min_creds": 96,},
	{"code": '25.62', "name": "Tecnología aeroespacial", "creds": 3, "min_creds": 96,},
	{"code": '25.63', "name": "Redes Neuronales", "creds": 3, "min_creds": 96,},
	{"code": '25.64', "name": "Deep Learning", "creds": 3, "min_creds": 96,},
	{"code": '25.65', "name": "Realidad Virtual", "creds": 3, "corr": [93.18, 25.03,]},
	{"code": '25.66', "name": "Acústica para Ingenieros", "creds": 3, "corr": [92.07,]},
	{"code": '25.67', "name": "Laboratorio de Dsp_fpga", "creds": 6, "corr": [25.17, 25.20,]},
	{"code": '25.68', "name": "Electrónica aplicada a Energías alternativas", "creds": 3, "corr": [25.28,]},
	{"code": '25.69', "name": "Introducción a la Investigación", "creds": 3, "min_creds": 183,},
	{"code": '25.70', "name": "Diseño analógico de circuitos integrados", "creds": 6, "corr": [25.56,]},
	{"code": '25.71', "name": "Diseño analógico de Sistemas integrados", "creds": 6, "corr": [25.70,]},
	{"code": '25.72', "name": "Diseño digital de circuitos integrados", "creds": 6,"corr": [25.56,]},
	{"code": '25.73', "name": "Verificación de Circuitos Digitales Integrados", "creds": 6,"corr": [25.72,]},
	{"code": '25.80', "name": "Introducción a la programación orientada a objetos", "creds": 3,},
	{"code": '25.81', "name": "Principios de Electrotecnia", "creds": 2,},
	{"code": '25.82', "name": "Circuitos de Audio", "creds": 2,},
	{"code": '25.83', "name": "Guías de ondas", "creds": 2,},
	{"code": '25.84', "name": "Convertidores de potencia", "creds": 2,},
	{"code": '25.85', "name": "Programación en bajo nivel", "creds": 2,},
	{"code": '25.86', "name": "Procesamiento Avanzado de Señales", "creds": 3,"corr": [25.53,]},
	{"code": '31.81', "name": "Tecnología de Máquinas", "creds": 6,},
	{"code": '31.99', "name": "Mecatrónica Aplicada", "creds": 3,},
	{"code": '94.24', "name": "Metodología del Aprendizaje", "creds": 3,},
	{"code": '94.42', "name": "Comunicación Estratégica", "creds": 3, "min_creds": 96},
]