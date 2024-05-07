import React, { useContext } from "react";
import { SummaryDataProps, Symbols } from "./Summary";
import useADCModuleConfig from "../adcComponentList/useADCModuleConfig";
import {
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";

export const useSummaryData = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);

  const VREFRDY = useBooleanSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTLINTENSET_VREFRDY`,
  });
  const VREFUPD = useBooleanSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTLINTENSET_VREFUPD`,
  });
  const VREFSelection = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTRLD_VREFSEL`,
  });
  const clockDivider = useIntegerSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_CTRLD_CTLCKDIV`,
  });

  const clockFrequecncy = useIntegerSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_INPUT_CLK_FREQ`,
  });

  const { adcModules } = useADCModuleConfig();
  let generalAdcConfig: Symbols[] = [
    {
      label: VREFSelection.label,
      value: VREFSelection.selectedOption,
    },
    { label: VREFRDY.label, value: VREFRDY.value ? "true" : "false" },
    { label: VREFUPD.label, value: VREFUPD.value ? "true" : "false" },
    { label: clockDivider.label, value: clockDivider.value },
    { label: clockFrequecncy.label, value: clockFrequecncy.value },
  ];

  const summaryData: SummaryDataProps[] = [
    {
      accordionHeader: "General ADC Config",
      summaryDetails: [
        {
          fieldSetHeader: "Genaral ADC Config",
          symbols: generalAdcConfig,
        },
      ],
    },
  ];
  adcModules.map(({ moduleId }) => {
    summaryData.push({
      accordionHeader: `ADC ${moduleId}`,
      summaryDetails: [
        {
          fieldSetHeader: `ADC_CORE ${moduleId}`,
          symbols: generalAdcConfig,
        },
      ],
    });
  });
  return {
    summaryData,
  };
};
