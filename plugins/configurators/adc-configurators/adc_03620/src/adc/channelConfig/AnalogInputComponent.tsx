import { SymbolIds } from "./ChannelConfigurationTable";
const AnalogInputComponent = (symbolId: SymbolIds) => {
  return (
    <div >
    {symbolId.index}
  </div>
  );
};

export default AnalogInputComponent;
