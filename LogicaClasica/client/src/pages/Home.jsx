import { FaComputer } from "react-icons/fa6";

export default function Home() {
  return (
    <div className="text-black min-h-screen p-8">
      <div className="container mx-auto text-center">
        <section className="h-screen flex items-center">
          <section className="w-1/2 text-center flex flex-col items-center">
            <FaComputer className="text-9xl text-black" />
          </section>
          <section className="text-center flex flex-col items-center">
            {/* Título principal */}
            <h1 className="text-2xl font-extrabold mb-8 tracking-tight leading-tight">
              Sistema Experto para Diagnóstico de Ordenadores
            </h1>

            {/* Sección de explicación general */}
            <div className="mb-16 px-4 sm:px-8 lg:px-16">
              <p className="text-lg font-light leading-relaxed max-w-4xl mx-auto">
                Bienvenido a nuestra herramienta de diagnóstico, donde
                utilizamos dos enfoques diferentes para identificar problemas en
                su ordenador: un{" "}
                <span className="font-bold text-blue-600">
                  sistema experto clásico
                </span>{" "}
                basado en reglas simples y un{" "}
                <span className="font-bold text-green-600">
                  sistema experto difuso
                </span>{" "}
                que maneja la incertidumbre en los síntomas.
              </p>
            </div>
          </section>
        </section>
        <hr className="border border-black/10" />
        <section className="h-screen flex flex-row gap-20 items-center">
          {/* Sección del sistema clásico */}
          <div>
            <h2 className="text-xl font-semibold mb-6 text-yellow-500">
              Sistema Experto Clásico
            </h2>
            <p className="text-lg font-light max-w-3xl mx-auto leading-relaxed">
              Este sistema se basa en un conjunto de reglas predefinidas que
              relacionan directamente los síntomas con las causas más probables.
              El sistema clásico puede ayudar a diagnosticar los siguientes
              problemas comunes:
            </p>
          </div>
          <ul className="list-disc list-inside text-left mx-auto mt-6 max-w-xl text-base leading-relaxed">
            <li className="mb-2">
              <span className="font-semibold text-yellow-500">Lentitud</span>:
              Falta de RAM, disco lleno o programas en segundo plano.
            </li>
            <li className="mb-2">
              <span className="font-semibold text-yellow-500">
                Reinicios inesperados
              </span>
              : Sobrecalentamiento, problemas de alimentación o errores del
              sistema operativo.
            </li>
            <li className="mb-2">
              <span className="font-semibold text-yellow-500">
                Problemas de red
              </span>
              : Falta de conexión a internet o configuración incorrecta.
            </li>
            <li className="mb-2">
              <span className="font-semibold text-yellow-500">
                Pantallazo azul (BSOD)
              </span>
              : Controladores mal instalados, hardware defectuoso.
            </li>
            <li className="mb-2">
              <span className="font-semibold text-yellow-500">
                Ruido extraño
              </span>
              : Ventilador o disco duro en mal estado.
            </li>
            <li className="mb-2">
              <span className="font-semibold text-yellow-500">No enciende</span>
              : Problemas de batería, fuente de alimentación o placa madre.
            </li>
          </ul>
        </section>
        <hr className="border border-black/10 shadow-xl" />
        <section className="h-screen flex flex-col justify-center items-center">
          {/* Sección del sistema difuso */}
          <div className="mb-16">
            <h2 className="text-xl font-semibold mb-6 text-green-600">
              Sistema Experto Difuso
            </h2>
            <p className="text-lg font-light mb-4 max-w-3xl mx-auto leading-relaxed">
              El sistema difuso maneja síntomas que no son absolutos, sino
              graduales, como la{" "}
              <span className="italic text-gray-700">
                &quot;lentitud leve&quot;
              </span>{" "}
              o la{" "}
              <span className="italic text-gray-700">
                &quot;temperatura moderadamente alta&quot;
              </span>
              . Utiliza un conjunto de reglas difusas que permite identificar
              problemas incluso cuando los síntomas no son claros.
            </p>
            <p className="text-lg font-light max-w-3xl mx-auto leading-relaxed">
              Con este enfoque, el diagnóstico no es simplemente{" "}
              <span className="font-semibold text-blue-400">
                &quot;bueno&quot;
              </span>{" "}
              o{" "}
              <span className="font-semibold text-red-400">
                &quot;malo&quot;
              </span>
              , sino que se genera un resultado en un rango que refleja el nivel
              de certeza del problema. Esto es especialmente útil cuando los
              síntomas no son evidentes o son ambiguos.
            </p>
          </div>
          {/* Llamada a la acción */}
          <div className="mt-16">
            <button className="bg-black hover:bg-gray-900 text-white font-bold py-3 px-6 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105">
              ¡Elige tu enfoque y comienza a diagnosticar ahora!
            </button>
          </div>
        </section>
      </div>
    </div>
  );
}
