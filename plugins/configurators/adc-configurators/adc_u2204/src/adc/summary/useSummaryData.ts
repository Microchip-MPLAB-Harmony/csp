import { SummaryDataProps ,Symbols} from "./Summary";
import useGenerealConfigurationSymbols from "../generalConfiguration/useGeneralConfigurationSymbols";
import useAnalogConfigurationSymbols from "../analogConfiguration/useAnalogConfigurationSymbols";
import useWindowComparisonSymbols from "../windowComparison/useWindowComparisonSymbols";

export const useSummaryData = () => {
  const {
    conversionTrigger,
    scanToStart,
    inputSCan,
    resultEvent,
    runStandby,
    leftAlignResult,
    resultInterrupt,
    preScaler,
    flushEvent,
    startEvent,
  } = useGenerealConfigurationSymbols();
  const {
    sampleLenght,
    reference,
    gain,
    conversionTime,
    channelConfigNegative,
    channelConfigPositve,
    resultResolution,
  } = useAnalogConfigurationSymbols();
  const { comparisonMode, win, winmonInterrupt, vlo, vhi } =
    useWindowComparisonSymbols();
    let generalAdcConfig: Symbols[] = [
      { label: conversionTrigger.label, value: conversionTrigger.value },
      {
        label: runStandby.label,
        value: runStandby.value === true ? "true" : "false",
      },
      { label: preScaler.label, value: preScaler.selectedOption },
      { label: scanToStart.label, value: scanToStart.value },
      { label: inputSCan.label, value: inputSCan.value },
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
      if (conversionTrigger.value === "HW Event Trigger") {
        generalAdcConfig.push(
          {
            label: startEvent.label,
            value: startEvent.value=== true ? "true" : "false",
          },
          {
            label: flushEvent.label,
            value: flushEvent.value=== true ? "true" : "false",
          }
        );
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
      {
        label: gain.label,
        value: gain.selectedOption,
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
          symbols: generalAdcConfig
        },
        {
          fieldSetHeader: "Analog Config",
          symbols:analogConfiguration ,
        },

        {
          fieldSetHeader: "Window Comparison",
          symbols:windowComparison
        },
      ],
    },
  ];
  return {
    summaryData,
  };
};
