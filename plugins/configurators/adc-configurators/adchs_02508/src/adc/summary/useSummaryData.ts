import { SummaryDataProps, Symbols } from "./Summary";
import useClockSourceSymbols from "../clockSource/useClockSourceSymbols";
import useReferenceVoltageSymbols from "../voltageReference/useReferenceVoltageSymbols";
import useADCModuleConfig from "../adcComponentList/useADCModuleConfig";

export const useSummaryData = () => {
  const { clockSource, labelTQ, frequency } = useClockSourceSymbols();
  const { voltageReference,endOfScan } = useReferenceVoltageSymbols();
  
  const {adcModules} = useADCModuleConfig();
  let generalAdcConfig: Symbols[] = [
    {
      label: clockSource.label,
      value: clockSource.selectedOption,
    },
    { label: frequency.label, value: frequency.value + "Hz" },
    {
      label: "ADCHS Clock",
      value:
        frequency.value === 0
          ? 0
          : ((1.0 / frequency.value) * 1000000000).toFixed(3) + "ns",
    },
    { label: "Control Clock", value: labelTQ.value.toFixed(3) + "ns" },
    { label: voltageReference.label, value: voltageReference.selectedOption },
    {label:endOfScan.label,value:endOfScan.value?'true':'false'}
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
  adcModules.map(({moduleId})=>{
    summaryData.push({accordionHeader: `ADC ${moduleId}`,
    summaryDetails: [{
      fieldSetHeader: `ADC ${moduleId}`,
      symbols: generalAdcConfig,
    },],})
  })

  summaryData.push({
    accordionHeader: "Channel Configuration",
    summaryDetails: [

    ],
  },)

  return {
    summaryData,
  };
};
