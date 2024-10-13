import Switch from "../components/Switch";
import { IoSend } from "react-icons/io5";
import { useState } from "react";
import { postQuery } from "../api/respuesta.api";

const listaPreguntas = [
  { pregunta: "¿Tu ordenador está lento?", codigoAsociado: "lentitud" },
  { pregunta: "¿El uso del CPU es alto?", codigoAsociado: "alto uso de CPU" },
  {
    pregunta: "¿El ordenador se reinicia inesperadamente?",
    codigoAsociado: "reinicios inesperados",
  },
  { pregunta: "¿Notas sobrecalentamiento?", codigoAsociado: "calentamiento" },
  {
    pregunta: "¿No tienes conexión a Internet?",
    codigoAsociado: "sin conexión",
  },
];

export default function LogicaStandard() {
  const [respuestas, setRespuestas] = useState([]);
  const [resultado, setResultado] = useState("");

  const handleEnviarRespuestas = async () => {
    const response = await postQuery({ sintomas: respuestas });
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
            className="mb-4 flex flex-row gap-5 items-center justify-center border border-black/10 p-4 rounded-2xl hover:shadow-lg transition-all duration-500"
          >
            <h2 className="text-lg flex font-semibold h-full text-black">
              {pregunta.pregunta}
            </h2>
            <Switch
              codigoAsociado={pregunta.codigoAsociado}
              setRespuestas={setRespuestas}
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
