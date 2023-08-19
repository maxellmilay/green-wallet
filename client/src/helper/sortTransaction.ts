import { TTransactionItem } from '../types/TTransaction';

const sortTransactions = (influx: TTransactionItem[], outflux: TTransactionItem[]) => {
  const combinedTransactions = [...influx, ...outflux];

  const sortedTransactions = combinedTransactions.sort(
    (objA, objB) => Number(objB.createdAt) - Number(objA.createdAt)
  );

  return sortedTransactions;
};

export default sortTransactions;
