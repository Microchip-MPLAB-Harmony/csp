import { SummaryDataProps, Symbols } from "./Summary";
import useGenerealConfigurationSymbols from "../generalConfiguration/useGeneralConfigurationSymbols";
import useWindowComparisonSymbols from "../windowComparison/useWindowComparisonSymbols";
import useAnalogConfigurationSymbols from "../analogConfiguration/useAnalogConfigurationSymbols";
import { PluginConfigContext, useBooleanSymbol } from "@mplab_harmony/harmony-plugin-client-lib";
import { useContext } from "react";

export const useSummaryData = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const {
    conversionTrigger,
    onDemandctrl,
    resultEvent,
    runStandby,
    leftAlignResult,
    resultInterrupt,
    preScaler,
    flushEvent,
    startEvent,
  } = useGenerealConfigurationSymbols();

  const { comparisonMode, win, winmonInterrupt, vlo, vhi } =
    useWindowComparisonSymbols();
  const {
    sampleLenght,
    reference,
    conversionTime,
    channelConfigNegative,
    channelConfigPositve,
    resultResolution,
  } = useAnalogConfigurationSymbols();
  const enableSlaveCheckBox = useBooleanSymbol({
    componentId,
    symbolId: "ADC_CTRLA_SLAVEEN",
  });

  let generalAdcConfig: Symbols[] = [
    {
      label: runStandby.label,
      value: runStandby.value === true ? "true" : "false",
    },
    {
      label: onDemandctrl.label,
      value: onDemandctrl.value === true ? "true" : "false",
    },
    {
      label: leftAlignResult.label,
      value: leftAlignResult.value === true ? "true" : "false",
    },
    {
      label: resultInterrupt.label,
      value: resultInterrupt.value === true ? "true" : "false",
    },
    {
      label: resultEvent.label,
      value: resultEvent.value === true ? "true" : "false",
    },
  ];
  if (!enableSlaveCheckBox.value) {
    generalAdcConfig.push(
      {
        label: preScaler.label,
        value: preScaler.selectedOption,
      },
      { label: conversionTrigger.label, value: conversionTrigger.value }
    );
    if (conversionTrigger.value === "HW Event Trigger") {
      generalAdcConfig.push(
        {
          label: startEvent.label,
          value: startEvent.selectedOption,
        },
        {
          label: flushEvent.label,
          value: flushEvent.selectedOption,
        }
      );
    }
  }
  let analogConfiguration: Symbols[] = [
    {
      label: channelConfigPositve.label,
      value: channelConfigPositve.selectedOption,
    },
    {
      label: channelConfigNegative.label,
      value: channelConfigNegative.selectedOption,
    },
    { label: sampleLenght.label, value: sampleLenght.value },
    { label: reference.label, value: reference.selectedOption },
    {
      label: "Conversion Time",
      value: conversionTime?.label
        ?.replace("**** Conversion Time is ", "")
        ?.replace(" ****", ""),
    },

    {
      label: resultResolution.label,
      value: resultResolution.selectedOption,
    },
  ];
  let windowComparison: Symbols[] = [
    { label: vhi.label, value: vhi.value },
    { label: vlo.label, value: vlo.value },

    {
      label: winmonInterrupt.label,
      value: winmonInterrupt.value === true ? "true" : "false",
    },
    { label: win.label, value: win.value === true ? "true" : "false" },
    {
      label: comparisonMode.label,
      value: comparisonMode.selectedOption,
    },
  ];
  const summaryData: SummaryDataProps[] = [
    {
      accordionHeader: "General ADC Config",
      summaryDetails: [
        {
          fieldSetHeader: "Genaral ADC Config",
          symbols: generalAdcConfig,
        },
        {
          fieldSetHeader: "Analog Config",
          symbols: analogConfiguration,
        },

        {
          fieldSetHeader: "Window Comparison",
          symbols: windowComparison,
        },
      ],
    },
    { accordionHeader: "DMA Sequencer", summaryDetails: [] },
  ];
  return {
    summaryData,
  };
};
