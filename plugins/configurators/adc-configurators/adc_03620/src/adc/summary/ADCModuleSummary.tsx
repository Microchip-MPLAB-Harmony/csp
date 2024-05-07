import { Fieldset } from "primereact/fieldset";
import {
  PluginConfigContext,
  createClassResolver,
  useBooleanSymbol,
  useCommentSymbol,
  useKeyValueSetSymbol,
  useStringSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { Symbols } from "./Summary";
import style from "./commonADCSummary.module.css";
import { useContext } from "react";
import ChannelConfigSummary from "./ChannelConfigSummary";
const cx = createClassResolver(style);
type Props = {
  accordionHeader: string;
};

const ADCModuleSummary = ({ accordionHeader }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const moduleId = accordionHeader.split(" ")[1];
  const channelEnable = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_ENABLE`,
  });
  const channelInterrupt = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_INTENSET_CHNERRC`,
  });
  const eventOutput = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_EVCTRL_RESRDYEO`,
  });
  const eventInput = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_EVCTRL_STARTEI`,
  });
  const endOfScanInterrupt = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_INTENSET_EOSRDY`,
  });
  const adcResult = useBooleanSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_PFFCTRL_PFFCR`,
  });
  const resolution = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_CORCTRL_SELRES`,
  });
  const triggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_CORCTRL_STRGSRC`,
  });
  const globalTriggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: `ADC_GLOBAL_PFFCTRL_PFFRDYDMA`,
  });
  const clckFreq = useCommentSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_ADC_CLOCK_FREQ`,
  });
  const actualRate = useStringSymbol({
    componentId,
    symbolId: `ADC_CORE_${moduleId}_ADC_CONVERSION_RATE`,
  });

  let generalAdcConfig: Symbols[] = [
    {
      label: channelInterrupt.label,
      value: channelInterrupt.value ? "true" : "false",
    },
    {
      label: eventOutput.label,
      value: eventOutput.value ? "true" : "false",
    },
    {
      label: resolution.label,
      value: resolution.selectedOption,
    },
    {
      label: eventInput.label,
      value: eventInput.value ? "true" : "false",
    },
    {
      label: endOfScanInterrupt.label,
      value: endOfScanInterrupt.value ? "true" : "false",
    },
    {
      label: adcResult.label,
      value: adcResult.value ? "true" : "false",
    },
    {
      label: triggerSource.label,
      value: triggerSource.selectedOption,
    },
    {
      label: globalTriggerSource.label,
      value: globalTriggerSource.selectedOption,
    },
    {
      label: "Sampling",
      value: clckFreq.label,
    },
    {
      label: actualRate.label,
      value: actualRate.value,
    },
  ];

  return (
    <div className={cx("summary-tab-container")}>
      {channelEnable.value ? (
        <>
          <Fieldset legend={accordionHeader}>
            {generalAdcConfig.map((symbol: Symbols) => (
              <div className={cx("summary-options")}>
                <div>{symbol.label}</div>
                <div>{symbol.value}</div>
              </div>
            ))}
          </Fieldset>
          <ChannelConfigSummary moduleId={moduleId} />
        </>
      ) : (
        "Channel Disabled"
      )}
    </div>
  );
};

export default ADCModuleSummary;
