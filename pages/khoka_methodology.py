import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__,path='/khoka_methodology')

# Define the navigation bar with the dropdown menu

portada =  dbc.Row(
        [
            html.Img(src="/assets/h_meto_1.webp",style={"width": "100%",'marginTop':'3%','marginBottom':'3   %'},className="center-image"),
        ]
                )

metodologia = dbc.Container(
    dbc.Row([
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("METODOLOGÍA", className="body-title-green"), 
                dbc.Row(className="espaciado_48_esc espaciado_48_mov"),
               html.Div(["En el jardín del Proyecto Khoka, ubicado en Medellín, Colombia, se recolectaron y secaron hojas de dos especies de ", html.Span("Erythroxylum", className="italic-text"), ", abarcando cuatro variedades distintas: E. ", html.Span("coca", className="italic-text"), " var. coca, E. ", html.Span("coca", className="italic-text"), " var. ", html.Span("ipadu", className="italic-text"), ", E. ", html.Span("novogranatense", className="italic-text"), " var. ", html.Span("novogranatense", className="italic-text"), " y E. ", html.Span("novogranatense", className="italic-text"), " var. ", html.Span("truxillense", className="italic-text"), ". De cada variedad se pesaron 100 gramos de hojas secas."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Mediante la técnica Soxhlet*, se prepararon tres tipos de extractos utilizando 300 mL de ", html.Span("disolventes", id="solvente_1",className="underlined-text"), " de distinta polaridad: etanol, diclorometano y hexano. Estos extractos se realizaron en triplicado y posteriormente se concentraron mediante destilación a presión reducida en un rotaevaporador RE100-pro de Biobase."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Los extractos concentrados se almacenaron en frascos ámbar y se enviaron al laboratorio MetCore de la Universidad de los Andes para su análisis. Allí, los extractos fueron procesados y conservados a -80 °C. Los análisis se llevaron a cabo utilizando un cromatógrafo de gases acoplado a un espectrómetro de masas con detector triple cuadrupolo, de la marca Agilent, referencia MS-QTOF 6545."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Img(src="/assets/h_meto_2.webp",style={"width": "100%"},className="center-image large-image"),
                html.Img(src="/assets/v_meto_2.webp",style={"width": "100%"},className="center-image small-image"),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Cromatografía de gases",className="body-title-2",id="meto_croma"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La cromatografía de gases es la técnica referente para la separación y el análisis de compuestos volátiles y es ampliamente utilizada en la determinación de gases, líquidos y sólidos. Para el análisis de sólidos, estos generalmente deben disolverse en un ", html.Span("solvente", id="solvente_2",className="underlined-text"), " volátil. Es adecuada para analizar compuestos orgánicos e inorgánicos cuyos pesos moleculares varían entre 2 y 1000 dáltones**."]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["Esta metodología es una de las más empleadas a nivel mundial. Por ejemplo, es posible separar hasta 400 compuestos de una sola muestra de café usando una columna capilar. Se puede utilizar con diversos tipos de detectores, siendo el detector de ionización de llama el más común. Este detector puede identificar concentraciones de hasta 50 partes por billón de compuestos orgánicos, con una desviación estándar del 5 % según McNair & Miller (1997)."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div("Tiempo de retención",className="body-title-2",id="meto_tiempo"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["En cromatografía líquida y de gases, el tiempo de retención se define como el intervalo que transcurre desde la inyección de una muestra al equipo, hasta el momento en que se registra la respuesta máxima por el detector. Este parámetro es crucial y se utiliza comúnmente para la identificación de compuestos en una mezcla analítica."]),
                dbc.Row(className="espaciado_96_esc espaciado_96_mov"),
                html.Div(["_______________"]),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["* ", html.Span("Técnica de extracción Soxhlet", className="italic-text"), ": es un método de separación que utiliza un disolvente líquido para extraer componentes de interés de una muestra sólida. Es ampliamente empleada para determinar el contenido graso en diversas muestras. El extractor Soxhlet, hecho de vidrio, incluye un condensador acoplado a una chaqueta que facilita el ingreso y la salida de agua."],className="footnote"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La muestra sólida se coloca dentro de un recipiente que está conectado a un sistema de sifón, similar al de las cisternas de inodoros. El proceso comienza calentando el ", html.Span("solvente", id="solvente_3",className="underlined-text"), " en un balón de fondo redondo, que está adaptado tanto al recipiente con el sifón como al condensador. Al alcanzar el punto de ebullición, el disolvente asciende por un canal hacia el condensador, donde se enfría y posteriormente gotea sobre la muestra. Cuando el nivel del ", html.Span("solvente", id="solvente_4",className="underlined-text"), " supera la entrada del sifón, se genera un vacío que lo impulsa de vuelta hacia el balón. Este ciclo se repite normalmente tres veces, y el tiempo total del proceso puede variar entre 6 y 18 horas, dependiendo del ", html.Span("solvente", id="solvente_5",className="underlined-text"), " utilizado."],className="footnote"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["** Dalton es la unidad de masa atómica unificada. Es una unidad estándar definida como un doceavo (1/12) de la masa de un átomo neutro y no enlazado de carbono-12, en su estado fundamental eléctrico y nuclear. Equivale a 1.6605402×10",html.Sup(-27)," kilogramos. Un mol de unidades de masa atómica es equivalente a un gramo. Un átomo de hidrógeno tiene una masa de 1.00784 dáltones, y una molécula de agua tiene una masa de 18.01528 dáltones."],className="footnote"),
                dbc.Row(className="espaciado_24_esc espaciado_24_mov"),
                html.Div(["La relación entre los valores de masa atómica y la masa macroscópica se establece a través del concepto de mol, que es la cantidad de unidades de una sustancia que contiene aproximadamente 6.0221367(36)x10",html.Sup(23),"entidades elementales, cifra que corresponde al valor numérico de la constante de Avogadro o número de Avogadro. Este número representa la cantidad total de átomos presentes en 12 gramos del isótopo de carbono-12. "],className="footnote"),
                
            ],
            className="container-text"
        ))

# Definir los tooltips
tooltips = []
# solvente
for i in range(1,6):
       tooltips.append(
              dbc.Tooltip("También llamado solvente, un disolvente es una sustancia, generalmente líquida, que puede disolver otras sustancias sin alterarlas químicamente para formar una solución.", 
                    target="solvente_{0}".format(str(i)), className="custom-tooltip"))




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
                metodologia,
                xs={"size": 12, "order": 4},  # Change order to 2 on extra small devices
                sm={"size": 12, "order": 4},  # Change order to 2 on small devices
                md={"size": 12, "order": 4},
                lg={"size": 12, "order": 4},
                xl={"size": 12, "order": 4},
                style={'paddingRight':'0rem','paddingLeft':'0rem'}
            ),
            *tooltips
        ]


