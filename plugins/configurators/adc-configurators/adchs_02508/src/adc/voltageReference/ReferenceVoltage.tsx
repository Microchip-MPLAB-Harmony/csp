import { KeyValueSetSymbolHook } from "@mplab_harmony/harmony-plugin-client-lib";
import { RadioButton, RadioButtonProps } from "primereact/radiobutton";
import { useEffect, useState } from "react";

const ReferenceVoltage = (
  props: RadioButtonProps & { keyValueSetSymbolHook: KeyValueSetSymbolHook } & {
    classPrefix: string;
    classResolver?: (className: string) => string;
  }
) => {
  const { options, readOnly, visible, writeValue, value } =
    props.keyValueSetSymbolHook;
  const {
    keyValueSetSymbolHook,
    classPrefix,
    classResolver,
    ...onlyRadioButtonProps
  } = props;
  const [avdd, setAvdd] = useState<boolean>(value === 0 || value === 2);
  const [vrefPlus, setVrefPlus] = useState<boolean>(value === 1 || value === 3);
  const [avss, setAvss] = useState<boolean>(value === 0 || value === 1);
  const [vrefMinus, setVrefMinus] = useState<boolean>(
    value === 2 || value === 3
  );
  useEffect(() => {
    switch (value) {
      case 0:
        setAvdd(true);
        setAvss(true);
        setVrefMinus(false);
        setVrefPlus(false);
        break;
      case 1:
        setAvdd(false);
        setAvss(true);
        setVrefMinus(false);
        setVrefPlus(true);
        break;
      case 2:
        setAvdd(true);
        setAvss(false);
        setVrefMinus(true);
        setVrefPlus(false);
        break;
      case 3:
        setAvdd(false);
        setAvss(false);
        setVrefMinus(true);
        setVrefPlus(true);
        break;
    }
  }, [value]);

  const onClicking = (value: string) => {
    switch (value) {
      case "AVDD":
        setAvdd(true);
        setVrefPlus(false);
        if (avss) {
          writeValue(options[0]);
        } else {
          writeValue(options[2]);
        }
        break;
      case "VREFH":
        setAvdd(false);
        setVrefPlus(true);
        if (vrefMinus) {
          writeValue(options[3]);
        } else {
          writeValue(options[1]);
        }
        break;
      case "AVSS":
        setAvss(true);
        setVrefMinus(false);
        if (avdd) {
          writeValue(options[0]);
        } else {
          writeValue(options[1]);
        }
        break;
      case "VREFL":
        setAvss(false);
        setVrefMinus(true);
        if (avdd) {
          writeValue(options[2]);
        } else {
          writeValue(options[3]);
        }
        break;
    }
  };

  return !(props.hidden ?? !visible) ? (
    <>
      <RadioButton
        inputId={options[0]}
        disabled={readOnly}
        value={"AVDD"}
        tooltip={"AVDD"}
        onChange={(e) => onClicking("AVDD")}
        checked={avdd}
        {...onlyRadioButtonProps}
        className={
          classResolver ? classResolver(`${classPrefix}0`) : `${classPrefix}0`
        }
      />
      <RadioButton
        inputId={options[1]}
        disabled={readOnly}
        value="VREFH"
        tooltip="VREF+"
        onChange={(e) => onClicking("VREFH")}
        checked={vrefPlus}
        {...onlyRadioButtonProps}
        className={
          classResolver ? classResolver(`${classPrefix}1`) : `${classPrefix}1`
        }
      />
      <RadioButton
        inputId={options[2]}
        disabled={readOnly}
        value="AVSS"
        tooltip="AVSS"
        onChange={(e) => onClicking("AVSS")}
        checked={avss}
        {...onlyRadioButtonProps}
        className={
          classResolver ? classResolver(`${classPrefix}2`) : `${classPrefix}2`
        }
      />
      <RadioButton
        inputId={options[3]}
        disabled={readOnly}
        value="VREFL"
        tooltip="VREF-"
        onChange={(e) => onClicking("VREFL")}
        checked={vrefMinus}
        {...onlyRadioButtonProps}
        className={
          classResolver ? classResolver(`${classPrefix}3`) : `${classPrefix}3`
        }
      />
    </>
  ) : (
    <></>
  );
};

export default ReferenceVoltage;
