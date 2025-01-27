import PlainLabel from "clock-common/lib/Components/LabelComponent/PlainLabel";
import { Button } from "primereact/button";
import { InputNumber } from "primereact/inputnumber";
import { useEffect, useState } from "react";
import {
  configSymbolApi,
  useIntegerSymbol,
  useKeyValueSetSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import { Dropdown } from "primereact/dropdown";
import { Divider } from "primereact/divider";
// import {
//   INPUT_MAX_FREQUENCY,
//   INPUT_MIN_FREQUENCY,
//   OUTPUT_MAX_FREQUENCY,
//   OUTPUT_MIN_FREQUENCY
// } from './FDPLLController';
const INPUT_MIN_FREQUENCY = 32768;
const INPUT_MAX_FREQUENCY = 2000000;
const OUTPUT_MIN_FREQUENCY = 48000000;
const OUTPUT_MAX_FREQUENCY = 96000000;
const FDPLLAutoCalculation = (props: {
  componentId: string;
  expectedOutputFreq: number;
  clockSourceItems: string[];
  selectedClockIndex: number;
  ldrInt: number;
  ldrFrac: number;
  dpllDiv: number;
  dpllPrescalar: number;
  dpllRefClock:any
  close: () => void;
}) => {
  const XOSC32K_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "XOSC32K_FREQ",
  });
  const XOSC_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "XOSC_FREQ",
  });
  const GCLK_ID_1_FREQ = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "GCLK_ID_1_FREQ",
  });

  const CONFIG_CLOCK_DPLL_LDR_INTEGER = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL_LDR_INTEGER",
  });

  const CONFIG_CLOCK_DPLL_DIVIDER = useIntegerSymbol({
    componentId: props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL_DIVIDER",
  });

  const [expectedOutput, setExpectedOutput] = useState<number>(
    props.expectedOutputFreq
  );
  const [clockSourceInput, setClockSourceInput] = useState<String>(
    props.clockSourceItems[props.selectedClockIndex]
  );
  const dpllRefClock = useKeyValueSetSymbol({
    componentId:props.componentId,
    symbolId: "CONFIG_CLOCK_DPLL_REF_CLOCK",
  });

  const [ldrInt, setLdrInt] = useState<number>(props.ldrInt);
  const [ldrFraction, setLdrFraction] = useState<number>(props.ldrFrac);
  const [fdpllOutputFreq, setFdpllOutputFreq] =
    useState<number>(expectedOutput);
  const [error, setError] = useState<number>(0.0);
  const [dpllPrescalar ,setDpllPescalar]=useState<number>(props.dpllPrescalar)
  const [clocksourceInputVal,setClocksourceInputVal]=useState<any>(props.selectedClockIndex)
  const accept = () => {
    configSymbolApi.setValue(
      props.componentId,
      "CONFIG_CLOCK_DPLL_LDR_INTEGER",
      ldrInt
    );
    configSymbolApi.setValue(
      props.componentId,
      "CONFIG_CLOCK_DPLL_LDRFRAC_FRACTION",
      ldrFraction
    );
    configSymbolApi.setValue(
      props.componentId,
      "CONFIG_CLOCK_DPLL_REF_CLOCK",
      clocksourceInputVal
    );
    configSymbolApi.setValue(
      props.componentId,
      "CONFIG_CLOCK_DPLL_PRESCALAR",
      dpllPrescalar
    );
    configSymbolApi.setValue(
      props.componentId,
      "CONFIG_CLOCK_DPLL_DIVIDER",
      CONFIG_CLOCK_DPLL_DIVIDER.value
    );

    props.close();
  };
  const cancel = () => {
    props.close();
  };
  useEffect(() => {
    newCalculate(expectedOutput);
    const temVal:any=props.dpllRefClock.optionPairs.filter((ele:any)=>ele.key===(clockSourceInput.split("(")[0].trim()))
    console.log(temVal)
    setClocksourceInputVal(temVal.value)
  }, [expectedOutput, clockSourceInput]);

  const targetFreqChanged = (newValue: any) => {
    setExpectedOutput(newValue);
    // newCalculate(newValue);
    // setButtonDisable(false);
  };

  const clockSourceChanged = (newValue: any) => {
    setClockSourceInput(newValue);
    
    // newCalculate(expectedOutput);
    // setButtonDisable(false);
  };

  const getInputFrequency = () => {
    let freq = 0;
    if (clockSourceInput.startsWith("XOSC32K")) {
      return XOSC32K_FREQ.value;
    } else if (clockSourceInput.startsWith("XOSC")) {
      freq = XOSC_FREQ.value / (2 * (props.dpllDiv + 1));
      return freq;
    } else if (clockSourceInput.startsWith("GCLK_DPLL")) {
      return GCLK_ID_1_FREQ.value;
    }
    return 0;
  };
  const invalidInput = () => {
    let i = getInputFrequency();
    return i < INPUT_MIN_FREQUENCY || i > INPUT_MAX_FREQUENCY;
  };
  const invalidOutput = () => {
    let i = expectedOutput;
    return i < OUTPUT_MIN_FREQUENCY || i > OUTPUT_MAX_FREQUENCY;
  };

  const newCalculate = (expectedOutput: number) => {
    let p1: Possibility | null = {
      ldrInt: props.ldrInt,
      ldrFraction: props.ldrFrac,
      fdpllOutputFreq: expectedOutput,
      prescalar:props.dpllPrescalar,
      error: 0,
    };
    let p2: Possibility | null = {
      ldrInt: props.ldrInt,
      ldrFraction: props.ldrFrac,
      fdpllOutputFreq: expectedOutput,
      prescalar:props.dpllPrescalar,
      error: 0,
    };
    let p3: Possibility | null = {
      ldrInt: props.ldrInt,
      ldrFraction: props.ldrFrac,
      fdpllOutputFreq: expectedOutput,
      prescalar:props.dpllPrescalar,
      error: 0,
    };

    let delta1 = 2147483647;
    let delta2 = 2147483647;
    let delta3 = 2147483647;

    let opFreq = expectedOutput;
    let ipFreq = getInputFrequency();

    let m1 = Math.round(((opFreq * 1) / ipFreq) * 1000) / 1000;
    let m2 = Math.round(((opFreq * 2) / ipFreq) * 1000) / 1000;
    let m3 = Math.round(((opFreq * 4) / ipFreq) * 1000) / 1000;

    if (m1 < 1) {
      // avoid m1 combination; because expected output freqency is less than achievable range
      p1 = null;
    } else {
      let i1 = Math.floor(m1 - 1);
      let f1 = Math.floor(Math.round((m1 - i1 - 1) * 16));

      if (
        i1 > CONFIG_CLOCK_DPLL_LDR_INTEGER.min &&
        i1 < CONFIG_CLOCK_DPLL_LDR_INTEGER.max
      ) {
        p1.ldrInt = i1;
        p1.ldrFraction = f1;
        p1.prescalar=1
        p1.fdpllOutputFreq = calculateOutputFreqency(
          ipFreq,
          p1.ldrInt,
          p1.ldrFraction,
          0
        );
        p1.error = Number(
          ((Math.abs(opFreq - p1.fdpllOutputFreq) * 100) / opFreq).toFixed(3)
        );
        delta1 = Math.abs(opFreq - p1.fdpllOutputFreq);
        if (p1.fdpllOutputFreq < OUTPUT_MIN_FREQUENCY) {
          let tempF1 = f1 + 1;
          p1 = fnreturnObtainedOutputFrequency(i1, tempF1, p1, ipFreq, opFreq);
        }
      } else {
        p1 = null;
      }
    }
    if (m2 < 1) {
      // avoid m1 combination; because expected output freqency is less than achievable range
      p2 = null;
    } else {
      let i2 = Math.floor(m2 - 1);
      let f2 = Math.floor(Math.round((m2 - i2 - 1) * 16));

      if (
        i2 > CONFIG_CLOCK_DPLL_LDR_INTEGER.min &&
        i2 < CONFIG_CLOCK_DPLL_LDR_INTEGER.max
      ) {
        p2.ldrInt = i2;
        p2.ldrFraction = f2;
        p2.prescalar=2;
        p2.fdpllOutputFreq = calculateOutputFreqency(
          ipFreq,
          p2.ldrInt,
          p2.ldrFraction,
          1
        );
        p2.error = Number(
          ((Math.abs(opFreq - p2.fdpllOutputFreq) * 100) / opFreq).toFixed(3)
        );
        delta2 = Math.abs(opFreq - p2.fdpllOutputFreq);
        if (p2.fdpllOutputFreq < OUTPUT_MIN_FREQUENCY) {
          let tempF2 = f2 + 1;
          p2 = fnreturnObtainedOutputFrequency(i2, tempF2, p2, ipFreq, opFreq);
      
        }
      } else {
        p2 = null;
      }
    }
    if (m3 < 1) {
      // avoid m1 combination; because expected output freqency is less than achievable range
      p3 = null;
    } else {
      let i3 = Math.floor(m3 - 1);
      let f3 = Math.floor(Math.round((m3 - i3 - 1) * 16));

      if (
        i3 > CONFIG_CLOCK_DPLL_LDR_INTEGER.min &&
        i3 < CONFIG_CLOCK_DPLL_LDR_INTEGER.max
      ) {
        p3.ldrInt = i3;
        p3.ldrFraction = f3;
        p3.prescalar=4
        p3.fdpllOutputFreq = calculateOutputFreqency(
          ipFreq,
          p3.ldrInt,
          p3.ldrFraction,
          2
        );
        p3.error = Number(
          ((Math.abs(opFreq - p3.fdpllOutputFreq) * 100) / opFreq).toFixed(3)
        );
        delta3 = Math.abs(opFreq - p3.fdpllOutputFreq);
        if (p3.fdpllOutputFreq < OUTPUT_MIN_FREQUENCY) {
          let tempF3 = f3 + 1;
          p3 = fnreturnObtainedOutputFrequency(i3, tempF3, p3, ipFreq, opFreq);
        }
      } else {
        p3 = null;
      }
    }
    if (
      p1 !== null &&
      (p1.fdpllOutputFreq === opFreq || (delta1 <= delta2 && delta1 <= delta3))
    ) {
      setLdrInt(p1.ldrInt);
      setLdrFraction(p1.ldrFraction);
      setFdpllOutputFreq(p1.fdpllOutputFreq);
      setDpllPescalar(divToPrescale(p1.prescalar))
      setError(p1.error);
      return;
    } else if (
      p2 !== null &&
      (p2.fdpllOutputFreq === opFreq || (delta2 <= delta1 && delta2 <= delta3))
    ) {
      setLdrInt(p2.ldrInt);
      setLdrFraction(p2.ldrFraction);
      setFdpllOutputFreq(p2.fdpllOutputFreq);
      setDpllPescalar(divToPrescale(p2.prescalar))
      setError(p2.error);
      return;
    } else if (
      p3 !== null &&
      (p3.fdpllOutputFreq === opFreq || (delta3 <= delta1 && delta3 <= delta2))
    ) {
      setLdrInt(p3.ldrInt);
      setLdrFraction(p3.ldrFraction);
      setFdpllOutputFreq(p3.fdpllOutputFreq);
      setDpllPescalar(divToPrescale(p3.prescalar))
      setError(p3.error);
      return;
    }
  };
  function calculateOutputFreqency(
    inputFrequency: number,
    ldrInt: number,
    ldrFraction: number,
    outputPrescale: number
  ): number {
    return (
      inputFrequency *
      (ldrInt + 1.0 + ldrFraction / 16.0) *
      (1.0 / Math.pow(2, outputPrescale))
    );
  }
  interface Possibility {
    ldrInt: number;
    ldrFraction: number;
    fdpllOutputFreq: number;
    error: number;
    prescalar:number
  }
  const fnreturnObtainedOutputFrequency = (
    i1: number,
    f1: number,
    p1: Possibility | null,
    ipFreq: number,
    opFreq: number
  ): Possibility | null => {
    if (!p1) return null;
    if (
      i1 > CONFIG_CLOCK_DPLL_LDR_INTEGER.min &&
      i1 < CONFIG_CLOCK_DPLL_LDR_INTEGER.max
    ) {
      p1.ldrInt = i1;
      p1.ldrFraction = f1;
      p1.fdpllOutputFreq = calculateOutputFreqency(
        ipFreq,
        p1.ldrInt,
        p1.ldrFraction,
        0
      );
      p1.error = (Math.abs(opFreq - p1.fdpllOutputFreq) * 100) / opFreq;
      if (p1.fdpllOutputFreq < OUTPUT_MIN_FREQUENCY ) {
        let f2 = f1 + 5;
        p1 = fnreturnObtainedOutputFrequency(i1, f2, p1, ipFreq, opFreq);
      }
    } else {
      p1 = null;
    }
    return p1;
  };
  function divToPrescale(div:number) {
    switch (div) {
        case 1:
            return 0;
        case 2:
            return 1;
        case 4:
            return 2;
        default:
            throw new Error("div value must be 1, 2, or 4, but given value is " + div);
    }
}

  return (
    <div>
      <div className="grid">
        <div className="col-6 text-right">
          <div className="flex flex-column">
            <PlainLabel
              disPlayText={"Desired DCO Output Frequency : "}
              className=""
            />
            <PlainLabel disPlayText={"(48 MHz to  96 MHz)"} className="" />
          </div>
        </div>
        <div className="col-6">
          <div className="flex flex-column">
            <div className="flex flex-row">
              <InputNumber
                value={expectedOutput}
                showButtons
                onValueChange={(target) => targetFreqChanged(target.value)}
              />
              <PlainLabel disPlayText={" Hz"} className={"m-2"} />
            </div>
            {invalidOutput() && (
              <PlainLabel
                className=""
                disPlayText={"Invalid Output Frequency Range ! ! !"}
                redColorStatus={true}
              />
            )}
          </div>
        </div>
      </div>
      <div className="grid">
        <div className="col-6  text-right">
          <div className="flex flex-column">
            <PlainLabel
              className=""
              disPlayText={"Select Reference Clock Source :"}
            />
            <PlainLabel className="" disPlayText={"(32 KHz to  2 MHz)"} />
          </div>
        </div>

        <div className="col-6">
          <div className="flex flex-column">
            <Dropdown
              value={clockSourceInput}
              options={props.clockSourceItems}
              onChange={(e) => clockSourceChanged(e.value)}
              // disabled={invalidOutput()}
            />
            {invalidInput() && (
              <PlainLabel
                className=""
                disPlayText={"Invalid Input Frequency Range ! ! !"}
                redColorStatus={true}
              />
            )}
          </div>
        </div>
      </div>
      <Divider />
      <div className="grid">
        <div className="col-6 text-right">
          <PlainLabel className="" disPlayText={"LDR Integer part :"} />
        </div>
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={ldrInt + ""} />
        </div>
      </div>
      <div className="grid">
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={"LDR Fractional part :"} />
        </div>
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={ldrFraction + ""} />
        </div>
      </div>
      {clockSourceInput === "XOSC (12 MHz)" && <div className="grid">
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={"XOSC Input Divider value :"} />
        </div>
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={props.dpllDiv + ""} />
        </div>
      </div>}
      <div className="grid">
        <div className="col-6  text-right">
          <PlainLabel
            className=""
            disPlayText={"Achievable DCO Output Freqency :"}
          />
        </div>
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={fdpllOutputFreq + ""} />
        </div>
      </div>
      <div className="grid">
        <div className="col-6  text-right">
          <PlainLabel
            className=""
            disPlayText={"Output Prescalar Value :"}
          />
        </div>
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={dpllPrescalar + ""} />
        </div>
      </div>
      <div className="grid">
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={"% Error :"} />
        </div>
        <div className="col-6  text-right">
          <PlainLabel className="" disPlayText={error + " %"} />
        </div>
      </div>
      <div className="flex flex-row-reverse">
        <div className="flex align-items-center justify-content-center m-2">
          <Button label={"Cancel"} onClick={cancel} />
        </div>
        <div className="flex align-items-center justify-content-center m-2">
          <Button
            label={"Accept"}
            onClick={accept}
            // disabled={buttonDisable}
          />
        </div>
      </div>
    </div>
  );
};
export default FDPLLAutoCalculation;
