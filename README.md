# Arqui1_Tarea2

Este proyecto implementa un simulador sencillo de **arquitectura de computadores**, mostrando la diferencia entre un procesador **CISC** y uno **RISC**.  

- El procesador **CISC** incluye instrucciones complejas como `SUMMEM` que realizan varias operaciones en un solo paso.  
- El procesador **RISC** descompone estas operaciones en instrucciones más simples como `TRAER`, `SUMAR` y `ESCRIBIR`.  


## 📂 Estructura del proyecto

```bash
Arqui1_Tarea2/
├── CISC.py       # Implementación del procesador CISC
├── RISC.py       # Implementación del procesador RISC
├── Mem.py        # Módulo de memoria
├── Alu.py        # Unidad aritmético-lógica
├── PC.py         # Contador de programa
├── Reg_mem.py    # Registros de propósito general (para RISC)
├── main.py       # Ejecución de pruebas
└── README.md     # Documentación del proyecto
```

---

## ⚙️ Instrucciones soportadas

### 🖥️ CISC
- `SUMMEM dest, dir1, dir2` → Suma dos valores de memoria (`dir1` y `dir2`) y guarda el resultado en `dest`.  
- `CMP dir1, dir2` → Compara dos valores de memoria y guarda el resultado en una bandera.  
- `BNE etiqueta` → Salta a una instrucción si los valores comparados no son iguales.  

### ⚡ RISC
- `TRAER Rn, dir` → Carga en el registro `Rn` el valor de memoria en `dir`.  
- `SUMAR Rdest, R1, R2` → Suma los valores de `R1` y `R2`, guardando el resultado en `Rdest`.  
- `ESCRIBIR dir, Rn` → Escribe en memoria (`dir`) el valor almacenado en el registro `Rn`.  

---