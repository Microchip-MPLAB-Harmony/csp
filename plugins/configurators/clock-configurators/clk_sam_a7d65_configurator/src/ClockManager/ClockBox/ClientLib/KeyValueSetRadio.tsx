import { KeyValueSetSymbolHook } from '@mplab_harmony/harmony-plugin-client-lib';
import { RadioButton, RadioButtonProps } from 'primereact/radiobutton';

const KeyValueSetRadio = (
  props: RadioButtonProps & { keyValueSetSymbolHook: KeyValueSetSymbolHook } & {
    classPrefix: string;
    radioNameClassPrefix?: string;
    classResolver?: (className: string) => string;
  }
) => {
  const { selectedOption, options, readOnly, visible, writeValue } = props.keyValueSetSymbolHook;
  const {
    keyValueSetSymbolHook,
    classPrefix,
    radioNameClassPrefix,
    classResolver,
    ...onlyRadioButtonProps
  } = props;

  return !(props.hidden ?? !visible) ? (
    <>
      {options.map((option, i) => (
        <RadioButton
          key={option}
          inputId={option}
          name={classPrefix}
          disabled={readOnly}
          value={option}
          tooltip={option}
          onChange={(e) => writeValue(option)}
          checked={option === selectedOption}
          {...onlyRadioButtonProps}
          className={classResolver ? classResolver(`${classPrefix}${i}`) : `${classPrefix}${i}`}
        />
      ))}
      {props.radioNameClassPrefix &&
        options.map((option, i) => (
          <label
            key={option}
            title={option}
            style={{ fontWeight: option === selectedOption ? 'bold' : 'initial' }}
            className={
              classResolver
                ? classResolver(`${radioNameClassPrefix}${i}`)
                : `${radioNameClassPrefix}${i}`
            }>
            {option}
          </label>
        ))}
    </>
  ) : (
    <></>
  );
};

export default KeyValueSetRadio;
