import { SymbolIds } from "./ChannelConfigurationTable";
const AnalogInputComponent = (symbolId: SymbolIds) => {
  return (
    <div >
    {symbolId.analogInput}
  </div>
  );
};

export default AnalogInputComponent;
