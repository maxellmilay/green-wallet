import { TItem } from '../types/TTransaction';

const sortTransactions = (transactions: TItem[]) => {
  const sortedTransactions = transactions.sort(
    (objA, objB) => Number(objB.created) - Number(objA.created)
  );

  return sortedTransactions;
};

export default sortTransactions;
