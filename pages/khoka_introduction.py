import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__,path='/')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_intro_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

introduccion = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_intr_img"),
                html.Div("INTRODUCCION", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["Desde la antigüedad, los componentes activos de la hoja de coca han despertado un profundo interés en el ser humano. Solo gracias a los avances en la ciencia química fue posible aislar su principal ", html.Span("alcaloide", id="alcaloide",className="underlined-text"), ", la cocaína, convirtiéndose en uno de los logros científicos más relevantes del siglo xix. Desde entonces, numerosos investigadores han buscado identificar los ", html.Span("compuestos químicos", id="compuestos_quimicos",className="underlined-text"), " presentes en sus distintas variedades. Entre ellos, Timothy Plowman, considerado el investigador sobre coca más importante del siglo xx, quien no solo clasificó botánicamente esta familia de plantas, sino que además llevó a cabo diversos estudios comparativos para conocer la composición química de cada variedad."]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Img(src="/assets/h_intro_2.webp",style={"width": "102%"},className="center-image large-image"),
                html.Img(src="/assets/h_intro_2.webp",style={"width": "100%"},className="center-image small-image"),
                html.Div([html.Span("Cortesía de The Field Museum of Chicago, USA.",className="footer-image footer-image-mobil" )]),
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
                html.Div(["Una revisión de la literatura académica existente sobre la composición química de esta familia de plantas revela que algunos de sus componentes podrían tener un gran potencial de aplicaciones, desde farmacológicas y alimenticias hasta agrícolas, evidenciando la importancia de continuar las investigaciones en este campo."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["En ",html.Span("Khoka Project", className="italic-text"), " hemos dedicado más de una década a cuidar de un jardín que alberga las cuatro variedades de coca que Plowman identificó a finales de los setenta como aquellas que han sido cultivadas y usadas ancestralmente por distintas culturas en Suramérica."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La familia de la coca abarca dos especies:"]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_intro_3.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/v_intro_3.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div(["Este estudio busca identificar qué compuestos químicos contienen las plantas de nuestro jardín. Las lecturas cromatográficas se realizaron en el laboratorio Met Core de la Universidad de los Andes en 2021 y los datos obtenidos fueron procesados, analizados y graficados por el equipo de ",html.Span("Khoka Project", className="italic-text"), "."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("¿Qué es la metabolómica?",className="body-title-2",id="intro_metabol_1"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La metabolómica es una rama de las ciencias naturales que se enfoca en el estudio detallado de los procesos metabólicos de los seres vivos, específicamente, a través del análisis de pequeñas ", html.Span("moléculas",id="moleculas_1", className="underlined-text")," conocidas como ",html.Span("metabolitos", className="italic-text"),", que son los compuestos producidos durante el metabolismo."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolismo en las Plantas",className="body-title-2",id="intro_metabol_2"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["El metabolismo es el conjunto de procesos químicos y físicos que tienen lugar en las células de los organismos vivos con el fin de transformar el alimento en ", html.Span("energía",id="energia_1",className="underlined-text"), " y poder llevar a cabo las funciones biológicas necesarias para preservar la vida: la respiración, la digestión, la circulación, la regulación de la temperatura corporal, la eliminación de desechos, etc."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_intro_4.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/v_intro_4.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div(["En las plantas, estos procesos incluyen funciones vitales como la fotosíntesis (donde la energía solar se transforma en energía química), la respiración, y la regulación de nutrientes, entre otros."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolitos",className="body-title-3",id="intro_metabol_3"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Los metabolitos son todas las sustancias producidas durante el metabolismo."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolismo primario",className="body-title-3",id="intro_metabol_p"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["El metabolismo primario en las plantas abarca todos los procesos físicos y químicos que convierten o consumen ", html.Span("energía",id="energia_2",className="underlined-text"), " y están directamente involucrados en su crecimiento, reproducción y supervivencia."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolismo secundario",className="body-title-3",id="intro_metabol_s"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["En las plantas se denomina metabolismo secundario a todo el conjunto de reacciones bioquímicas que cumplen funciones vitales no relacionadas con el crecimiento o la reproducción."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Las plantas destinan una cantidad significativa del carbono asimilado y de su ", html.Span("energía",id="energia_3",className="underlined-text"), " a la ", html.Span("síntesis",id="sintesis_2",className="underlined-text"), " de una amplia variedad de ", html.Span("moléculas",id="moleculas_2",className="underlined-text"), " orgánicas que no participan directamente en la fotosíntesis, la respiración, la asimilación de nutrientes, el transporte de ", html.Span("solutos",id="solutos",className="underlined-text"), " o en la ", html.Span("síntesis",id="sintesis_1",className="underlined-text"), " de ", html.Span("proteínas",id="proteinas",className="underlined-text"), ", carbohidratos o lípidos."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La gran mayoría de metabolitos secundarios desempeñan funciones de protección. Esta protección puede ser contra la radiación ultravioleta, cambios fuertes de temperatura, daño ", html.Span("oxidativo",id="oxidativo",className="underlined-text"), ", contra el ataque de microorganismos, como hongos y bacterias; de herbívoros, como insectos, reptiles, aves o mamíferos; e incluso frente a otras plantas."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Las principales rutas de producción de estos metabolitos secundarios en las plantas provienen del metabolismo primario del carbono. Estos compuestos también son conocidos como productos naturales y poseen un valor significativo tanto en el ámbito medicinal como económico. Este último se deriva de su uso en diversas industrias, incluyendo la cosmética, alimentaria, farmacéutica y agrícola."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Los metabolitos secundarios son compuestos químicos de bajo peso molecular y de naturaleza diversa que por sus propiedades (tóxicas, ", html.Span("narcóticas",id="narcoticas",className="underlined-text"), ", ", html.Span("sedantes",id="sedantes",className="underlined-text"), ", etc.) se han utilizado con fines medicinales, insecticidas, repelentes y cosméticos, entre otros."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Metabolómica en la investigación de la coca",className="body-title-2L",id="intro_metabol_4"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Estudiar la planta de coca desde un enfoque metabolómico implica expandir la comprensión que tenemos sobre la química de esta planta, indagando acerca de los distintos metabolitos que esta produce y sus posibles aplicaciones industriales, farmacológicas y terapéuticas."]),
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []
# compuesto químico
tooltips.append(
    dbc.Tooltip("Un compuesto químico es una sustancia formada por la unión de dos o más elementos \
                diferentes de la tabla periódica. Cada compuesto se caracteriza por una fórmula química \
                específica que indica la composición exacta de sus elementos. Por ejemplo, el agua (H2O) \
                está compuesta por dos átomos de hidrógeno y uno de oxígeno.", target="compuestos_quimicos", 
                className="custom-tooltip"))

# Alcaloide
tooltips.append(dbc.Tooltip("Los alcaloides son compuestos naturales que las plantas producen mediante el metabolismo secundario. Estos contienen nitrógeno en su estructura molecular y son conocidos por sus potentes efectos sobre el cuerpo, incluso en dosis pequeñas. Se utilizan en medicina para aliviar el dolor y tratar enfermedades mentales. Ejemplos destacados de alcaloides incluyen la cafeína en el café y la nicotina en el tabaco, ambos estimulantes; la cocaína de la planta de coca, que además es un anestésico local; y la morfina de la amapola, empleada como analgésico.", 
                    target="alcaloide", className="custom-tooltip"))

# Moléculas
for i in range(1,3):
       tooltips.append(dbc.Tooltip("Una molécula es una agrupación definida de dos o más átomos unidos químicamente, que constituye la unidad más pequeña de una sustancia química pura y conserva todas sus propiedades características. Las moléculas pueden variar en tamaño desde simples diatómicas, como el oxígeno molecular (O2), hasta macromoléculas complejas como el ADN y las proteínas, que pueden contener decenas a miles de átomos unidos en estructuras específicas. Los enlaces que mantienen unidos los átomos en una molécula pueden ser covalentes, donde los átomos comparten electrones, o iónicos, donde los átomos se atraen debido a cargas opuestas. Esta estructura y composición definen las propiedades físicas y químicas de la sustancia.", 
                    target="moleculas_{0}".format(str(i)), className="custom-tooltip"))

# Energía
for i in range(1,4):
       tooltips.append(dbc.Tooltip("La energía es la capacidad para realizar trabajo o inducir cambios físicos, es una propiedad fundamental de la naturaleza que se manifiesta en diferentes formas, como mecánica, térmica, eléctrica, química, nuclear y otras. Esta capacidad puede ser transferida entre sistemas y convertida de una forma a otra, pero no puede ser creada ni destruida (primera ley de la termodinámica).", 
                    target="energia_{0}".format(str(i)), className="custom-tooltip"))

# Síntesis
for i in range(1,3):
       tooltips.append(dbc.Tooltip("La síntesis química es el proceso por el cual se crean compuestos químicos complejos a partir de reactivos más simples mediante reacciones químicas controladas. Este proceso es fundamental en la química para la fabricación de numerosos productos, desde medicamentos hasta materiales avanzados. La síntesis química implica la formación de enlaces químicos y se lleva a cabo siguiendo métodos y técnicas específicos que permiten obtener el producto deseado con alta pureza y rendimiento. Es utilizada tanto en investigación como en la industria para desarrollar nuevas sustancias y mejorar las propiedades de las ya existentes.", 
                    target="sintesis_{0}".format(str(i)), className="custom-tooltip"))

# Solutos
tooltips.append(dbc.Tooltip("Soluto es la sustancia que se disuelve en otra sustancia, conocida como disolvente, para formar una solución. El soluto es generalmente la sustancia en menor cantidad en una mezcla, aunque esto puede variar dependiendo de la solución.", 
                    target="solutos", className="custom-tooltip"))

# Proteínas
tooltips.append(dbc.Tooltip("Las proteínas son macromoléculas complejas y esenciales que desempeñan una variedad de funciones críticas dentro de los organismos vivos. Están formadas por cadenas lineales de aminoácidos, cuya secuencia está determinada por los nucleótidos en los genes correspondientes del ADN. Estas secuencias de aminoácidos se pliegan en estructuras tridimensionales específicas que determinan la función de la proteína. Las proteínas son indispensables para prácticamente todos los procesos biológicos, incluyendo la catalización de reacciones metabólicas (enzimas), la regulación de la expresión génica, la transmisión de señales entre y dentro de las células, el soporte estructural en células, tejidos, y el transporte de moléculas a través de membranas celulares. Además, las proteínas juegan un papel crucial en el sistema inmunitario y en el movimiento muscular. Debido a su diversidad funcional y su rol en la base de muchas patologías, son objeto central de numerosas investigaciones en biomedicina y biotecnología.", 
                    target="proteinas", className="custom-tooltip"))

# Oxidativo
tooltips.append(dbc.Tooltip("La oxidación es el proceso químico mediante el cual un átomo, ión o molécula pierde electrones durante una reacción química. Tradicionalmente, este término se asociaba con las reacciones donde el oxígeno se combinaba con otras sustancias, incrementando así el contenido de oxígeno del compuesto. Sin embargo, en un sentido más amplio, la oxidación no necesariamente involucra oxígeno. Se define modernamente en química como la pérdida de electrones, lo cual puede afectar las propiedades químicas de la sustancia involucrada y a menudo ocurre simultáneamente con la reducción, donde otra sustancia gana los electrones perdidos en el proceso de oxidación. Este conjunto de procesos complementarios se conoce como reacción redox (reducción-oxidación).", 
                    target="oxidativo", className="custom-tooltip"))

# Narcóticos
tooltips.append(dbc.Tooltip("El término narcótico se utiliza generalmente para describir sustancias que inducen sueño, relajación muscular, y una pérdida de la sensibilidad y la conciencia. En el contexto médico, los narcóticos son una clase de medicamentos que en su mayoría son analgésicos opioides, que se utilizan principalmente para el manejo del dolor severo. Estos compuestos actúan en el sistema nervioso central para aliviar el dolor, pero también pueden suprimir la respiración, causar somnolencia y, a menudo, dependencia física y psicológica si se usan inadecuadamente o durante períodos prolongados. Ejemplos comunes incluyen morfina, fentanilo y codeína.", 
                    target="narcoticas", className="custom-tooltip"))

# Sedantes
tooltips.append(dbc.Tooltip("Un sedante es una sustancia o combinación de sustancias que ejercen un efecto relajante sobre el sistema nervioso central. Los sedantes son comúnmente utilizados para tratar trastornos como la ansiedad y el insomnio, ayudando a reducir la tensión, la agitación y facilitando el sueño. Estos fármacos pueden variar en potencia, desde ligeros sedantes que ayudan a relajar al paciente, hasta hipnóticos más potentes que inducen el sueño.", 
                    target="sedantes", className="custom-tooltip"))




# Define the layout
layout =    [ dbc.Col(
                portada,
                xs={"size": 12, "order": 2},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 2},  # Change order to 2 on small devices
                md={"size": 12, "order": 3},
                lg={"size": 12, "order": 3},
                xl={"size": 12, "order": 3},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
                
            ),
            dbc.Col(
                introduccion,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


