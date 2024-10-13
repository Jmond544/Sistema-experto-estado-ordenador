import { IoSend } from "react-icons/io5";
import { useState } from "react";
import { postQueryDifuso } from "../api/respuesta.api";
import ButtonGroup from "../components/ButtonGroup";

const listaPreguntas = [
  {
    pregunta: "¿Tu ordenador está lento?",
    codigoAsociado: "lentitud",
    titles: ["baja", "media", "alta"],
  },
  {
    pregunta: "¿El uso del CPU?",
    codigoAsociado: "uso_cpu",
    titles: ["bajo", "medio", "alto"],
  },
  {
    pregunta: "¿El ordenador se reinicia?",
    codigoAsociado: "reinicios",
    titles: ["pocos", "moderados", "frecuentes"],
  },
  {
    pregunta:
      "¿Cómo describirías la temperatura del ordenador?",
    codigoAsociado: "temperatura",
    titles: ["fría", "normal", "caliente"],
  },
];

export default function LogicaDifusa() {
  const [respuestas, setRespuestas] = useState([]);
  const [resultado, setResultado] = useState("");
  const [selected, setSelected] = useState({
    lentitud: "",
    uso_cpu: "",
    reinicios: "",
    temperatura: "",
  });

  console.log(selected);

  const handleEnviarRespuestas = async () => {
    const response = await postQueryDifuso(selected);
    setResultado(response.diagnostico);
  };

  return (
    <div className="py-24 mx-auto flex flex-col items-center">
      <h1 className="font-bold mb-4 text-2xl">Formulario</h1>
      <p className=" mb-4">
        Completa el siguiente cuestionario para diagnosticar tu ordenador
      </p>
      {listaPreguntas.map((pregunta, index) => {
        return (
          <div
            key={index}
            className="min-w-96 mb-4 flex flex-col gap-5 items-center justify-center border border-black/10 p-4 rounded-2xl hover:shadow-lg transition-all duration-500"
          >
            <h2 className="text-lg flex font-semibold h-full text-black">
              {pregunta.pregunta}
            </h2>
            <ButtonGroup
              titles={pregunta.titles}
              nameItem={pregunta.codigoAsociado}
              selected={selected}
              setSelected={setSelected}
            />
          </div>
        );
      })}
      <button
        onClick={handleEnviarRespuestas}
        className="bg-black px-4 py-2 text-white text-xl font-bold rounded-full flex gap-2 items-center"
      >
        <p>Enviar respuestas</p>
        <IoSend className="text-2xl inline" />
      </button>
      {resultado && (
        <div className="mt-8">
          <h2 className="text-2xl font-bold mb-4">Resultado</h2>
          <p className="text-lg">{resultado}</p>
        </div>
      )}
    </div>
  );
}
