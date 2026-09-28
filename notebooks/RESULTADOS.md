# Modelo XGBoost B3 — Horizonte 5 dias

## Sumário

Modelo de previsão de retorno relativo ao mercado em horizonte de 5 dias.
Features de preço, volume, técnicos, cross-sectional e macro.
Validação: split temporal + backtest long-short.

## Performance (Q4 2024, teste out-dez)

### Métricas de ML
- AUC: **0.5469**
- IC (Spearman): **0.0649** (p=0.0009)
- Features: 60

### Backtest (top/bottom 5%, long-short)
- Retorno bruto:       +4.35%
- Retorno LÍQUIDO:     +1.60%  (após custo de 0.05%/trade)
- Retorno buy&hold:    -73.07%
- Max drawdown:        -2.03%
- Sharpe líquido:      **2.13**
- Calmar:              **3.71**
- Dias batendo BH:     44/55

## Comparação com horizonte de 1 dia

| Métrica | 1d | 5d | Ganho |
|---|---|---|---|
| AUC | 0.5171 | 0.5469 | +0.0298 |
| IC | 0.0423 | 0.0649 | +0.0226 |
| Retorno liq | -23.5% | +1.60% | virada |
| Sharpe liq | 0.45 | 2.13 | +1.68 |

## Configuração

- XGBoost: n_estimators=500, max_depth=3, learning_rate=0.02
- Subsample 0.7, colsample 0.7, min_child_weight=50
- Reg_alpha=0.5, reg_lambda=2.0
- Top/bottom 5% por ranking cross-sectional diário

## Limitações

1. Amostra curta (55 dias no teste)
2. Sem validação walk-forward completa
3. Sem teste em outros anos (2022, 2023)
4. Sharpe pode estar inflado pelo método de cálculo

## Próximos passos

1. Testar em 2023 e 2022 (validação out-of-sample real)
2. Walk-forward completo com horizonte de 5d
3. Ensemble: XGBoost + LightGBM + CatBoost
4. Features fundamentalistas (P/L, ROE, dívida)
5. Reduzir para top/bottom 3% (menos trades, mais seletivo)
