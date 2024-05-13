import { ConfigSymbol, symbolUtilApi } from '@mplab_harmony/harmony-plugin-client-lib';

let maxChannel: number | undefined;

const getMaxChannel = async (componentId: string, symbolId: string): Promise<number> => {
  if (maxChannel) return maxChannel;

  const symbolIds = await symbolUtilApi.getChildren(componentId, symbolId);

  const symbols = (await symbolUtilApi.getSymbols(componentId, symbolIds)) as ConfigSymbol<any>[];

  const channelNumbers = symbols
    .filter((e) => e.symbolType === 'BooleanSymbol')
    .filter((e) => e.label.includes('Select AN'))
    .map((e) => e.label.replace('Select AN', '').replace(' for Input Scan', ''))
    .map((e) => parseInt(e));

  maxChannel = Math.max(...channelNumbers);

  return maxChannel;
};

export { getMaxChannel };
