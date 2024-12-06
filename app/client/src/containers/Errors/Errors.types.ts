import { ErrorProps } from "../../components/Error";

export type ErrorsProps = {
  status: number;
};

export type ErrorConfig = {
  [key: number]: ErrorProps;
};
