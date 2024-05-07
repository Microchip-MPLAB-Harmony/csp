import { Fieldset } from "primereact/fieldset";
import {
  PluginConfigContext,
  createClassResolver,
  useBooleanSymbol,
  useFloatSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import {  Symbols } from "./Summary";
import style from "./commonADCSummary.module.css";
import { useContext } from "react";
const cx = createClassResolver(style);
type Props = {
  accordionHeader: string;
};

const ADCModuleSummary = ({ accordionHeader }: Props) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const moduleId = accordionHeader.split(" ")[1];
  const channelEnable = useBooleanSymbol({
    componentId,
    symbolId: `ADCHS_${moduleId}_ENABLE`,
  });
  const pinConfigPositive = useKeyValueSetSymbol({
    componentId,
    symbolId:
      moduleId !== "7" ? `ADCTRGMODE__SH${moduleId}ALT` : `ADCTRGMODE__SH0ALT`,
  });
  const pinConfigNegative = useBooleanSymbol({
    componentId,
    symbolId:
      moduleId !== "7" ? `ADCIMCON1__DIFF${moduleId}` : `ADCIMCON1__DIFF0`,
  });
  const tad = useFloatSymbol({
    componentId,
    symbolId: `ADCHS_TADC${moduleId}`,
  });
  const resolution = useKeyValueSetSymbol({
    componentId,
    symbolId: moduleId !== "7" ? `ADC${moduleId}TIME__SELRES`:`ADCCON1__SELRES`,
  });
  const conversionRate = useFloatSymbol({
    componentId,
    symbolId: `ADCHS_CONV_RATE${moduleId}`,
  });
  const triggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId:
      moduleId !== "7" ? `ADCTRG1__TRGSRC${moduleId}` : `ADCTRG1__TRGSRC0`,
  });
  const inputScan = useBooleanSymbol({
    componentId,
    symbolId: moduleId !== "7" ? `ADCCSS1__CSS${moduleId}` : `ADCCSS1__CSS0`,
  });
  const signMode = useBooleanSymbol({
    componentId,
    symbolId:
      moduleId !== "7" ? `ADCIMCON1__SIGN${moduleId}` : `ADCIMCON1__SIGN0`,
  });
  const diffMode = useBooleanSymbol({
    componentId,
    symbolId:
      moduleId !== "7" ? `ADCIMCON1__DIFF${moduleId}` : `ADCIMCON1__DIFF0`,
  });
  const interrupt = useBooleanSymbol({
    componentId,
    symbolId:
      moduleId !== "7" ? `ADCGIRQEN1__AGIEN${moduleId}` : `ADCGIRQEN1__AGIEN0`,
  });

  const scanTriggerSource = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADCCON1__STRGSRC",
  });

  let generalAdcConfig: Symbols[] = [
    {
      label: channelEnable.label,
      value: channelEnable.value ? "true" : "false",
    },
    {
      label: tad.label,
      value: tad.value,
    },
    {
      label: resolution.label,
      value: resolution.selectedOption,
    },
    {
      label: conversionRate.label,
      value: conversionRate.value,
    },
  ];

  if (moduleId < "7") {
    generalAdcConfig.push(
      {
        label: pinConfigPositive.label,
        value: pinConfigPositive.selectedOption,
      },
      {
        label: pinConfigNegative.label,
        value: pinConfigNegative.value ? "true" : "false",
      },
      {
        label: triggerSource.label,
        value: triggerSource.selectedOption,
      },
      {
        label: inputScan.label,
        value: inputScan.value ? "true" : "false",
      },
      {
        label: signMode.label,
        value: signMode.value ? "true" : "false",
      },
      {
        label: diffMode.label,
        value: diffMode.value ? "true" : "false",
      },
      {
        label: interrupt.label,
        value: interrupt.value ? "true" : "false",
      }
    );
  }
  if (moduleId === "7") {
    generalAdcConfig.push({
      label: scanTriggerSource.label,
      value: scanTriggerSource.selectedOption,
    });
  }

  return (
    <div className={cx("summary-tab-container")}>
      {channelEnable.value ? (
        <Fieldset legend={accordionHeader}>
          {generalAdcConfig.map((symbol: Symbols) => (
            <div className={cx("summary-options")}>
              <div>{symbol.label}</div>
              <div>{symbol.value}</div>
            </div>
          ))}
        </Fieldset>
      ) : (
        "Channel Disabled"
      )}
    </div>
  );
};

export default ADCModuleSummary;
