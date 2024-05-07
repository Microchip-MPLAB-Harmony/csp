import { SummaryDataProps, Symbols } from "./Summary";
import useGenerealConfigurationSymbols from "../generalConfiguration/useGeneralConfigurationSymbols";
import useWindowComparisonSymbols from "../windowComparison/useWindowComparisonSymbols";
import useTriggerSymbols from "../trigger/useTriggerSymbols";

export const useSummaryData = () => {
  const {
    resultSign,
    prescaler,
    fifoChunkSize,
    clockFrequency,
    clockFrequencyWarning,
    sleepMode,
    fastWakeUp,
    enableFifo,
    fifoEnableLevel,
  } = useGenerealConfigurationSymbols();

  const {
    comparisonMode,
    comparisonType,
    windowComparisonBoolean,
    interrupt,
    channelCombo,
    vlo,
    vhi,
  } = useWindowComparisonSymbols();
  const { triggerMode, triggerPeriod, triggerSelection } = useTriggerSymbols();
  let generalAdcConfig: Symbols[] = [
    {
      label: prescaler.label,
      value: prescaler.value,
    },
    { label: resultSign.label, value: resultSign.selectedOption },
    { label: sleepMode.label, value: sleepMode.value ? "true" : "false" },
    { label: enableFifo.label, value: enableFifo.value ? "true" : "false" },
    {
      label: clockFrequency.label,
      value: clockFrequency.value,
    },
  ];
  if (sleepMode.value) {
    generalAdcConfig.push({ label: fastWakeUp.label, value: fastWakeUp.value });
  }
  if (enableFifo.value) {
    generalAdcConfig.push(
      { label: fifoEnableLevel.label, value: fifoEnableLevel.selectedOption },
      { label: fifoChunkSize.label, value: fifoChunkSize.value }
    );
  }
  if (clockFrequencyWarning.visible) {
    generalAdcConfig.push({
      label: "Clock Warning",
      value: clockFrequencyWarning.label,
    });
  }
  const windowComparison: Symbols[] = [
    {
      label: windowComparisonBoolean.label,
      value: windowComparisonBoolean.value ? "true" : "false",
    },
  ];
  if (windowComparisonBoolean.value) {
    windowComparison.push(
      {
        label: comparisonMode.label,
        value: comparisonMode.selectedOption,
      },
      {
        label: comparisonType.label,
        value: comparisonType.selectedOption,
      },
      {
        label: interrupt.label,
        value: interrupt.value ? "true" : "false",
      },
      { label: channelCombo.label, value: channelCombo.value },
      { label: vlo.label, value: vlo.value },
      { label: vhi.label, value: vhi.value }
    );
  }

  const triggerConfig: Symbols[] = [
    {
      label: triggerMode.label,
      value: triggerMode.selectedOption,
    },
  ];

  if ([1, 2, 3].includes(triggerMode.value)) {
    triggerConfig.push({
      label: triggerSelection.label,
      value: triggerSelection.selectedOption,
    });
  }
  if (triggerMode.value === 4) {
    triggerConfig.push({
      label: triggerPeriod.label,
      value: triggerPeriod.value,
    });
  }
  const summaryData: SummaryDataProps[] = [
    {
      accordionHeader: "General ADC Config",
      summaryDetails: [
        {
          fieldSetHeader: "Genaral ADC Config",
          symbols: generalAdcConfig,
        },

        {
          fieldSetHeader: "Window Comparison",
          symbols: windowComparison,
        },
        {
          fieldSetHeader: "Trigger Config",
          symbols: triggerConfig,
        },
      ],
    },
    {
      accordionHeader: "Channel Sequencer",
      summaryDetails: [],
    },
    {
      accordionHeader: "Channel Configuration",
      summaryDetails: [],
    },
  ];

  return {
    summaryData,
  };
};
