import { instanceAxios } from "./axiosInstance.js";

export const postQuery = async ({ sintomas }) => {
  try {
    const response = await instanceAxios.post("/diagnostico", {
      sintomas,
    });
    console.log(response);
    return response.data;
  } catch (error) {
    console.error(error);
    return error;
  }
};
