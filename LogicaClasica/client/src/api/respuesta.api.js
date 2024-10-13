import { instanceAxios } from "./axiosInstance.js";

export const postQueryClasica = async ({ sintomas }) => {
  try {
    const response = await instanceAxios.post("/diagnostico-clasico", {
      sintomas,
    });
    console.log(response);
    return response.data;
  } catch (error) {
    console.error(error);
    return error;
  }
};

export const postQueryDifuso = async ({
  lentitud,
  uso_cpu,
  reinicios,
  temperatura,
}) => {
  try {
    const response = await instanceAxios.post("/diagnostico-difuso", {
      lentitud,
      uso_cpu,
      reinicios,
      temperatura,
    });
    console.log(response);
    return response.data;
  } catch (error) {
    console.error(error);
    return error;
  }
};
