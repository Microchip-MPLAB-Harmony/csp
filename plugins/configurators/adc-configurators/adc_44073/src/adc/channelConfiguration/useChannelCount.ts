import { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  stringSymbolApi,
  integerSymbolApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { ChannelIds } from "./ChannelConfigurationTable";
export type ChannelIdObject= {
  channel: string[],
  enable:string [],
  signalName: string[],
  positiveInput: string[],
  negativeInput:string [],
  interrupt: string[],
  gain:string[],
  offset:string[]
}
const useChannelCount = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [MAX_CH_COUNT, setMAX_CH_COUNT] = useState<number>(0);
  const [productFamily, setProductFamily] = useState<string>("");
  const [channelIds, setChannelIds] = useState<ChannelIds[]>([]);
  const [channelIdObject,setChannelIdObject] = useState<ChannelIdObject>({
    channel: [],
    enable: [],
    signalName: [],
    positiveInput: [],
    negativeInput: [],
    interrupt: [],
    gain:[],
    offset:[]
  })
  
  useEffect(() => {
    stringSymbolApi.getValue("core", "PRODUCT_FAMILY").then((e) => {
      setProductFamily(e);
    });
    integerSymbolApi.getValue(componentId, "ADC_NUM_CHANNELS").then((e) => {
      setMAX_CH_COUNT(e);
    });
  }, []);

  useEffect(() => {
    const channelId: ChannelIds[] = Array.apply(null, Array(MAX_CH_COUNT)).map(
      (e, i) => {
        return {
          index: i,
          channel: `CH${i}`,
          enable: `ADC_${i}_CHER`,
          signalName: `ADC_${i}_NAME`,
          positiveInput: `ADC_${i}_POS_INP`,
          negativeInput: `ADC_${i}_NEG_INP`,
          interrupt: `ADC_${i}_IER_EOC`,
          gain:`ADC_${i}_CGR_GAIN`,
          offset:`ADC_${i}_COR_OFFSET`
        };
      }
    );
    setChannelIds(channelId);
  }, [MAX_CH_COUNT]);
  
  useEffect(()=>{
    const keys = Object.keys(channelIdObject);
    channelIds.forEach(function (a) {
      keys.forEach(function (k) {
        channelIdObject[k as keyof ChannelIdObject].push(a[k as keyof ChannelIdObject]);
      });
    });
    channelIdObject.enable=JSON.parse(JSON.stringify(channelIdObject.enable))
    setChannelIdObject(channelIdObject)
  },[channelIds])
  

  
  return {
    MAX_CH_COUNT,
    channelIds,
    productFamily,
    channelIdObject
  };
};

export default useChannelCount;
