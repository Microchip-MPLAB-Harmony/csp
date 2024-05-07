import { useContext, useEffect, useState } from "react";
import {
  PluginConfigContext,
  stringSymbolApi,
  integerSymbolApi,
  symbolUtilApi,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { SymbolIds } from "./ChannelConfigurationTable";
export type SymbolIdsObject = {
  analogInput: string[];
  enable: string[];
  signedMode: string[];
  diffMode: string[];
  triggerSource: string[];
  inputScan: string[];
  interrupt: string[];
};
const useSymbolControl = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [NUM_CHANNELS_COUNT, setNUM_CHANNELS_COUNT] = useState<number>(0);
  const [NUM_SIGNALS_COUNT, setNUM_SIGNALS_COUNT] = useState<number>(0);
  const [NUM_CLASS1_SIGNALS_COUNT, setNUM_CLASS1_SIGNALS_COUNT] =
    useState<number>(0);
  const [NUM_CLASS2_SIGNALS_COUNT, setNUM_CLASS2_SIGNALS_COUNT] =
    useState<number>(0);
  const [class1Menu, setclass1Menu] = useState<string[]>([]);
  const [class2Menu, setclass2Menu] = useState<string[]>([]);
  const [class3Menu, setclass3Menu] = useState<string[]>([]);
  const [class2andClass3Menu, setclass2andClass3Menu] = useState<string[]>([]);
  const [symbolIds, setSymbolIds] = useState<SymbolIds[]>([]);
  useEffect(() => {
    const urls = [
      integerSymbolApi.getValue(componentId, "ADCHS_NUM_CHANNELS"),
      integerSymbolApi.getValue(componentId, "ADCHS_NUM_SIGNALS"),
      integerSymbolApi.getValue(componentId, "ADCHS_NUM_CLASS2_SIGNALS"),
      integerSymbolApi.getValue(componentId, "ADCHS_NUM_CLASS1_SIGNALS"),
    ];
    const MenuUrls = [
      symbolUtilApi.getChildren(componentId, "ADCHS_CLASS1_SIGNALS_CONF"),
      symbolUtilApi.getChildren(componentId, "ADCHS_CLASS2_SIGNALS_CONF"),
      symbolUtilApi.getChildren(componentId, "ADCHS_CLASS3_SIGNALS_CONF"),
    ];

    const fetchMenuData = async () => {
      try {
        const responses = await Promise.all(MenuUrls.map((url) => url));
        const data = await Promise.all(responses.map((response) => response));
        setclass1Menu(data[0]);
        setclass2Menu(data[1]);
        setclass3Menu(data[2]);
      } catch (error) {
        console.error(error);
      }
    };

    fetchMenuData();

    const fetchData = async () => {
      try {
        const responses = await Promise.all(urls.map((url) => url));
        const data = await Promise.all(responses.map((response) => response));
        setNUM_CHANNELS_COUNT(data[0]);
        setNUM_SIGNALS_COUNT(data[1]);
        setNUM_CLASS2_SIGNALS_COUNT(data[2]);
        setNUM_CLASS1_SIGNALS_COUNT(data[3]);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [componentId]);
  useEffect(() => {
    setclass2andClass3Menu([...class2Menu, ...class3Menu]);
  }, [class2Menu, class3Menu]);

  useEffect(() => {
    const symbolIds: any[] = [];
    class2andClass3Menu.map((analogInput: string) => {
      symbolIds.push({
        analogInput: analogInput,
        enable: analogInput,
        signedMode: getSignedModeSymbolId(analogInput),
        diffMode: getDiffModeSymbolId(analogInput),
        interrupt: getInterruptSymbolId(analogInput),
        inputScan: getScanInputSymbolId(analogInput),
        triggerSource: getTriggerSymbolId(analogInput),
      });
    });
    setSymbolIds(symbolIds);
  }, [class2andClass3Menu]);

  const getSignedModeSymbolId = (analogInput: string) => {
    const index = analogInput.replace(/[^0-9]/g, "");
    if (parseInt(index) < 16) {
      return `ADCIMCON1__SIGN${index}`;
    }
    if (parseInt(index) >= 16 && parseInt(index) < 32) {
      return `ADCIMCON2__SIGN${index}`;
    }
    if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
      return `ADCIMCON3__SIGN${index}`;
    }
  };
  const getDiffModeSymbolId = (analogInput: string) => {
    const index = analogInput.replace(/[^0-9]/g, "");
    if (parseInt(index) < 16) {
      return `ADCIMCON1__DIFF${index}`;
    }
    if (parseInt(index) >= 16 && parseInt(index) < 32) {
      return `ADCIMCON2__DIFF${index}`;
    }
    if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
      return `ADCIMCON3__DIFF${index}`;
    }
  };

  const getInterruptSymbolId = (analogInput: string) => {
    const index = analogInput.replace(/[^0-9]/g, "");
    if (parseInt(index) < 32) {
      return `ADCGIRQEN1__AGIEN${index}`;
    }
    if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
      return `ADCGIRQEN2__AGIEN${index}`;
    }
  };
  const getScanInputSymbolId = (analogInput: string) => {
    const index = analogInput.replace(/[^0-9]/g, "");
    if (parseInt(index) < 32) {
      return `ADCCSS1__CSS${index}`;
    }
    if (parseInt(index) >= 32 && parseInt(index) < NUM_SIGNALS_COUNT) {
      return `ADCCSS2__CSS${index}`;
    }
  };

  const getTriggerSymbolId = (analogInput: string) => {
    const index = analogInput.replace(/[^0-9]/g, "");
    if (parseInt(index) < 4) {
      return `ADCTRG1__TRGSRC${index}`;
    }
    if (parseInt(index) >= 4 && parseInt(index) < 8) {
      return `ADCTRG2__TRGSRC${index}`;
    }
    if (parseInt(index) >= 8 && parseInt(index) < 12) {
      return `ADCTRG3__TRGSRC${index}`;
    }
    if (parseInt(index) >= 12 && parseInt(index) < 16) {
      return `ADCTRG4__TRGSRC${index}`;
    }
    if (parseInt(index) >= 16 && parseInt(index) < 20) {
      return `ADCTRG5__TRGSRC${index}`;
    }
    if (parseInt(index) >= 20 && parseInt(index) < 24) {
      return `ADCTRG6__TRGSRC${index}`;
    }
    if (parseInt(index) >= 24 && parseInt(index) < NUM_SIGNALS_COUNT) {
      return `ADCTRG7__TRGSRC${index}`;
    }
  };
  return {
    NUM_CHANNELS_COUNT,
    NUM_SIGNALS_COUNT,
    class2andClass3Menu,
    symbolIds,
  };
};

export default useSymbolControl;
