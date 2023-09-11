// export type TTransactionItem = {
//   id: number;
//   createdAt: Date;
//   name: string;
//   value: number;
// };

// export type TTransaction = {
//   name: string;
//   influx: TTransactionItem[];
//   outflux: TTransactionItem[];
// };

export type TGroup = {
  uuid: string;
  name: string;
  owner: string;
  income: number;
  expenses: number;
  balance: number;
  created: string;
};

export type TItem = {
  uuid: string;
  name: string;
  group: string;
  amount: number;
  created: string;
};
