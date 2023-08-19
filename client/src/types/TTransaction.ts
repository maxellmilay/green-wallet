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
