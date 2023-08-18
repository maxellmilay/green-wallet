export type TTransactionItem = {
  id: number;
  createdAt: Date;
  name: string;
  value: number;
};

export type TTransaction = {
  name: string;
  influx: TTransactionItem[];
  outflux: TTransactionItem[];
};

export type TItemPayload = {
  type: string;
  description: string;
  value: number;
};

export type TTransactionPayload = {
  type: string;
  name: string;
};
